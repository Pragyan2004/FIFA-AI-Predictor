# FIFA World Cup 2026 AI Predictor

An enterprise-grade AI football analytics platform. This platform uses machine learning pipelines (LangChain & Groq LLMs) and live data (via worldcup26.ir REST API) to deliver unparalleled match forecasting, live tracking, and sports analytics.

## Features
- **Live Match Center**: Real-time scores and tournament tracking via official broadcasting endpoints.
- **AI Analytics Dashboard**: View live model confidence, value betting alerts, and Expected Golden Boot projections.
- **AI Match Prediction**: Run simulated matchups between countries using LLM-driven analytics and historical head-to-head metrics.
- **Enterprise UI**: Modern, glassmorphic dashboard interface fully responsive on mobile and desktop.

## Prerequisites
- Python 3.9+
- A [Groq API Key](https://console.groq.com/) for the AI prediction engine.

## Installation & Local Setup

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
   Create a `.env` file in the root directory and add your Groq API key:
   ```env
   GROQ_API_KEY=your_api_key_here
   ```

4. **Run the Application:**
   ```bash
   python app.py
   ```
   Access the web application at `http://127.0.0.1:5000`.

## Docker Deployment

This project includes a `Dockerfile` for seamless cloud or on-premise deployment.

1. **Build the Docker Image:**
   ```bash
   docker build -t fifa-ai-predictor .
   ```

2. **Run the Container:**
   ```bash
   docker run -p 5000:5000 --env-file .env fifa-ai-predictor
   ```
   Access the application at `http://localhost:5000`.

## Tech Stack
- **Backend:** Flask, Python
- **AI/ML:** LangChain, Groq (Llama-3), Pandas
- **Frontend:** HTML5, Tailwind CSS
- **Data Source:** [worldcup26.ir API](https://github.com/rezarahiminia/worldcup2026)
