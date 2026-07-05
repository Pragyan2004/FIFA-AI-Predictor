---
title: FIFA World Cup 2026 AI Predictor
emoji: ⚽
colorFrom: blue
colorTo: pink
sdk: docker
app_port: 7860
pinned: false
license: mit
---

# 🏆 FIFA World Cup 2026 AI Predictor

**Enterprise-grade FIFA World Cup 2026 AI analytics platform. Harness live API data and machine learning to simulate matches, forecast Golden Boot winners, and surface real-time tactical value bets.**

## 📊 Model & Application Details
- **Architecture:** Flask (Python backend) with Tailwind CSS (Frontend)
- **AI/ML Engine:** LangChain orchestration with Groq's LLaMA-3 (70B) for high-speed tactical simulations.
- **Data Source:** Integration with the open-source `worldcup26.ir` REST API for real-time fixtures, team stats, and match progress.
- **Deployment:** Containerized via Docker for seamless cloud deployment.

## 🎯 Intended Use
This platform is designed for sports analysts, fantasy football managers, and football enthusiasts to:
1. View live match scores and tournament progression in real-time.
2. Run AI-driven simulations of specific matches (Group Stage, Knockouts) based on historical head-to-head metrics and recent team form.
3. Access tactical betting insights and "Upset Alerts" surfaced by our ML pipeline.
4. Track predicted Golden Boot leaders based on Expected Goals (xG).

## 🚀 Installation & Local Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Pragyan2004/FIFA-AI-Predictor.git
   cd FIFA-AI-Predictor
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables:**
   Create a `.env` file in the root directory and add your [Groq API key](https://console.groq.com/):
   ```env
   GROQ_API_KEY=your_api_key_here
   ```

4. **Run the Application:**
   ```bash
   python app.py
   ```
   Access the web application at `http://127.0.0.1:5000`.

## 🐳 Docker Deployment

This project includes a `Dockerfile` optimized for production deployment on platforms like Hugging Face Spaces, Render, or AWS.

1. **Build the Docker Image:**
   ```bash
   docker build -t fifa-ai-predictor .
   ```

2. **Run the Container:**
   ```bash
   docker run -p 5000:5000 --env-file .env fifa-ai-predictor
   ```

## ⚠️ Limitations & Bias
- **Data Dependency:** The LLM's predictions heavily rely on the static historical CSV dataset (`archive.zip`) and dynamic updates from `worldcup26.ir`. If an underdog team rapidly improves over a few months, the historical data might lag in capturing this momentum.
- **Hallucinations:** While the system prompt is strictly constrained to output JSON, underlying LLM generations regarding match tactical narratives can occasionally hallucinate player injuries or unverified squad inclusions. 
- **Not Financial Advice:** The "Value Bets" and predictions provided are purely for analytical and entertainment purposes.

## 🤝 Contributing
Contributions are highly welcome! Feel free to open issues or submit pull requests for new analytical widgets, performance improvements, or UI refinements.

## 📄 License
This project is licensed under the MIT License.
