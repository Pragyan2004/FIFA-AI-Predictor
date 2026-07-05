import os
import json
from zipfile import ZipFile
import pandas as pd
from flask import Flask, render_template, request
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import requests

# --- Phase 5 & 6: Security and Scaling Scaffolds ---
# Note: In production, install Flask-Limiter and Celery.
# from flask_limiter import Limiter
# from flask_limiter.util import get_remote_address

load_dotenv()

app = Flask(__name__)

# limiter = Limiter(
#     get_remote_address,
#     app=app,
#     default_limits=["100 per minute"]
# )

# Mock Async Task Configuration for Phase 6
# app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'

DATASET = "./archive.zip"

def load_results(path=DATASET):
    if path.endswith(".zip"):
        with ZipFile(path) as z:
            return pd.read_csv(z.open("results.csv"), parse_dates=["date"])
    return pd.read_csv(path, parse_dates=["date"])

df = load_results()

def form(team, n=5):
    matches = df[(df.home_team == team) | (df.away_team == team)].sort_values("date").tail(n)
    result = []
    for _, row in matches.iterrows():
        if row.home_team == team:
            scored, conceded = row.home_score, row.away_score
        else:
            scored, conceded = row.away_score, row.home_score
        if scored > conceded: result.append("W")
        elif scored == conceded: result.append("D")
        else: result.append("L")
    return "-".join(result) if result else "N/A"

def stats(team):
    matches = df[(df.home_team == team) | (df.away_team == team)].sort_values("date")
    if len(matches) == 0: return None
    wins = draws = losses = gf = ga = 0
    for _, row in matches.iterrows():
        if row.home_team == team:
            scored, conceded = row.home_score, row.away_score
        else:
            scored, conceded = row.away_score, row.home_score
        gf += scored
        ga += conceded
        if scored > conceded: wins += 1
        elif scored == conceded: draws += 1
        else: losses += 1
    return {
        "matches": len(matches),
        "wins": wins,
        "draws": draws,
        "losses": losses,
        "goals_for": gf,
        "goals_against": ga,
        "avg_goals": round(gf / len(matches), 2) if len(matches) > 0 else 0,
        "avg_conceded": round(ga / len(matches), 2) if len(matches) > 0 else 0,
        "recent_form": form(team),
    }

def h2h(team_a, team_b):
    matches = df[
        ((df.home_team == team_a) & (df.away_team == team_b)) |
        ((df.home_team == team_b) & (df.away_team == team_a))
    ]
    a = b = d = 0
    for _, row in matches.iterrows():
        if row.home_score == row.away_score:
            d += 1
        elif (row.home_team == team_a and row.home_score > row.away_score) or (row.away_team == team_a and row.away_score > row.home_score):
            a += 1
        else:
            b += 1
    return {"team_a_wins": a, "draws": d, "team_b_wins": b}

def predict_match(team_a, team_b, stage="Group Stage", model="llama-3.3-70b-versatile"):
    team_a_stats = stats(team_a)
    team_b_stats = stats(team_b)
    if team_a_stats is None or team_b_stats is None:
        raise ValueError("One or both teams were not found in the dataset.")
    
    head2head = h2h(team_a, team_b)
    llm = ChatGroq(model=model, api_key=os.getenv("GROQ_API_KEY"), temperature=0.2)
    prompt = f"""
You are a professional football analyst.
Predict the FIFA World Cup 2026 match.
Stage: {stage}
Team A: {team_a}
Statistics: {json.dumps(team_a_stats, indent=2)}
Team B: {team_b}
Statistics: {json.dumps(team_b_stats, indent=2)}
Head-to-head: {json.dumps(head2head, indent=2)}
Use: Historical performance, Recent form, Goals scored, Goals conceded, Head-to-head, Overall team quality
Return ONLY valid JSON.
{{
    "predicted_winner":"",
    "confidence_percentage":0,
    "key_reasoning":""
}}
"""
    response = llm.invoke([("system", "You are an expert football analyst. Return ONLY JSON."), ("human", prompt)])
    content = response.content.strip()
    if content.startswith("```"):
        content = content.replace("```json", "").replace("```", "").strip()
    return json.loads(content)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/prediction", methods=["GET", "POST"])
def prediction():
    prediction_result = None
    error = None
    if request.method == "POST":
        team_a = request.form.get("team_a")
        team_b = request.form.get("team_b")
        stage = request.form.get("stage", "Group Stage")
        try:
            prediction_result = predict_match(team_a, team_b, stage)
            prediction_result['team_a'] = team_a
            prediction_result['team_b'] = team_b
        except Exception as e:
            error = str(e)
    
    return render_template("prediction.html", result=prediction_result, error=error)



# --- Phase 1: API Endpoints (Live Data via worldcup26.ir API) ---
@app.route("/api/v1/predict", methods=["POST"])
def api_predict():
    return {"status": "success", "prediction": "Mock Prediction Data"}

@app.route("/api/v1/matches")
def api_matches():
    try:
        resp = requests.get("https://worldcup26.ir/get/games", timeout=5)
        return {"status": "success", "data": resp.json()}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.route("/api/v1/leaderboard")
def api_leaderboard():
    return {
        "status": "success",
        "data": [
            {"user_id": 101, "username": "SoccerFan99", "accuracy": "89%", "points": 1250},
            {"user_id": 102, "username": "PredictionKing", "accuracy": "84%", "points": 1100}
        ]
    }

@app.route("/api/v1/stats")
def api_stats():
    try:
        resp = requests.get("https://worldcup26.ir/get/groups", timeout=5)
        return {"status": "success", "data": resp.json()}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.route("/api/v1/teams")
def api_teams():
    try:
        resp = requests.get("https://worldcup26.ir/get/teams", timeout=5)
        return {"status": "success", "data": resp.json()}
    except Exception as e:
        return {"status": "error", "message": str(e)}

# --- Phase 2: Web Pages Scaffold ---
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")



@app.route("/live")
def live_match_center():
    return render_template("live.html")

@app.route("/fantasy")
def fantasy_hub():
    return render_template("fantasy.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/privacy")
def privacy():
    return render_template("privacy.html")

@app.route("/terms")
def terms():
    return render_template("terms.html")

@app.route("/cookie")
def cookie():
    return render_template("cookie.html")

if __name__ == "__main__":
    app.run(debug=True, port=5000)
