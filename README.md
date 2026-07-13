# 🚀 Hybrid Token-Efficient AI Routing Agent

> AMD Developer Hackathon 2026 – Track 1 Submission

An intelligent AI routing system that dynamically selects the most efficient Large Language Model (LLM) based on prompt complexity, task type, confidence, and token usage. By avoiding unnecessary use of large models, it reduces inference cost, latency, and token consumption while maintaining response quality.

---

## 🌟 Features

- 🧠 Automatic prompt classification
- 📊 Complexity estimation
- 🤖 Intelligent model selection
- 📈 Confidence scoring
- 🔄 Automatic model escalation
- 💰 Token-efficient routing
- ⚡ FastAPI REST API
- 🎨 React + TypeScript + Vite frontend
- 🔥 Fireworks AI integration
- 📦 Docker support
- 🧪 Benchmark & evaluation scripts
- 📊 Token usage analytics

---

## 🏗️ Project Architecture

```
User Prompt
     │
     ▼
Intent Classifier
     │
     ▼
Complexity Estimator
     │
     ▼
Routing Policy
     │
     ▼
Selected LLM
     │
     ▼
Fireworks AI API
     │
     ▼
Confidence Validator
     │
     ▼
Escalation (if required)
     │
     ▼
Final Response
```

---

## 🤖 Supported Models

- GPT-OSS-120B
- Qwen3 30B
- DeepSeek V3

---

## 🛠️ Tech Stack

### Backend

- Python
- FastAPI
- HTTPX
- Pydantic
- Fireworks AI API

### Frontend

- React
- TypeScript
- Vite

### Deployment

- Render (Backend)
- Vercel (Frontend)

---

## 📁 Project Structure

```
Hybrid-Routing-Agent/

├── app/
│   ├── api/
│   ├── classifier/
│   ├── router/
│   ├── validator/
│   ├── fireworks/
│   ├── analytics/
│   ├── schemas.py
│   ├── config.py
│   └── main.py
│
├── frontend/
│   ├── src/
│   ├── package.json
│   └── vite.config.ts
│
├── evaluation/
├── tests/
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── README.md
└── LICENSE
```

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/abhi262020/hybrid-token-efficient-routing-agent.git

cd hybrid-token-efficient-routing-agent
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create environment file

```bash
cp .env.example .env
```

Example `.env`

```env
APP_NAME=Hybrid Token-Efficient Routing Agent

FIREWORKS_API_KEY=YOUR_FIREWORKS_KEY

FIREWORKS_BASE_URL=https://api.fireworks.ai/inference/v1

DEFAULT_MODEL=accounts/fireworks/models/gpt-oss-120b

CONFIDENCE_THRESHOLD=0.85

MAX_TOKENS=512

TEMPERATURE=0.2
```

Run backend

```bash
python -m uvicorn app.main:app --reload
```

Run frontend

```bash
cd frontend

npm install

npm run dev
```

---

## 📡 API

### POST `/route`

Request

```json
{
  "prompt": "Explain Quantum Computing"
}
```

Example Response

```json
{
  "model": "accounts/fireworks/models/gpt-oss-120b",
  "task": "general",
  "complexity": 2,
  "confidence": 0.91,
  "tokens": 196,
  "response": "Quantum computing is..."
}
```

---

## 📊 Evaluation

Run benchmarks

```bash
python evaluation/benchmark.py
```

Compare models

```bash
python evaluation/compare_models.py
```

Token analysis

```bash
python evaluation/token_analysis.py
```

---

## 🧪 Testing

```bash
pytest
```

---

## 🐳 Docker

Build and run

```bash
docker compose up --build
```

---

## 🌐 Live Demo

Frontend

> https://your-vercel-url.vercel.app

Backend

> https://your-render-url.onrender.com

API Docs

> https://your-render-url.onrender.com/docs

---

## 🎯 Hackathon Objective

This project demonstrates an adaptive AI routing strategy that intelligently selects the most suitable language model based on task complexity. Instead of always using the largest model, it balances quality, speed, and cost through dynamic routing and confidence-based escalation.

---

## 🔮 Future Improvements

- Multi-provider routing (OpenAI, Fireworks, Groq)
- Semantic prompt caching
- Streaming responses
- RAG integration
- User authentication
- Real-time analytics dashboard
- Cost estimation dashboard
- Model performance leaderboard

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Abhishek J S**

GitHub: https://github.com/abhi262020

AMD Developer Hackathon 2026
