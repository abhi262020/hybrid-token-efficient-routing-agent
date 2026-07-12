# 🚀 Hybrid Token-Efficient Routing Agent

> AMD Developer Hackathon 2026 – Track 1

An intelligent AI routing system that automatically selects the most cost-effective Large Language Model (LLM) based on prompt complexity, task type, confidence, and token efficiency. Built with **FastAPI**, **React**, and **Fireworks AI** on **AMD infrastructure**.

---

## 📌 Overview

Most AI applications send every request to the largest available model, resulting in unnecessary cost and latency.

Hybrid Token-Efficient Routing Agent solves this by analyzing each prompt and dynamically routing it to the most appropriate LLM.

The system performs:

- Intent Classification
- Complexity Estimation
- Model Selection
- AI Response Generation
- Confidence Validation
- Automatic Escalation
- Token Analytics

This enables faster inference, lower API costs, and improved scalability without sacrificing response quality.

---

## ✨ Features

- Intelligent prompt classification
- Complexity estimation
- Dynamic LLM routing
- Confidence-based validation
- Automatic model escalation
- Token usage analytics
- REST API using FastAPI
- Modern React + Vite frontend
- Fireworks AI integration
- AMD Hackathon ready

---

## 🏗 Architecture

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
Select Best Model
     │
     ▼
Fireworks AI
     │
     ▼
Response Validator
     │
     ▼
Confidence Check
     │
     ▼
Escalation (if required)
     │
     ▼
Final Response
```

---

## 🤖 Supported Models

| Model | Purpose |
|--------|----------|
| GPT-OSS-120B | Complex reasoning |
| Qwen3-30B | Medium complexity |
| Llama 3.1 8B | Lightweight tasks |

---

## 🛠 Tech Stack

### Backend

- Python
- FastAPI
- Fireworks AI API
- HTTPX
- Pydantic

### Frontend

- React
- TypeScript
- Vite
- CSS

### AI

- GPT-OSS-120B
- Fireworks AI
- Token Analytics
- Dynamic Routing

---

## 📁 Project Structure

```
HybridRouter/
│
├── app/
│   ├── api/
│   ├── classifier/
│   ├── router/
│   ├── fireworks/
│   ├── validator/
│   ├── analytics/
│   └── main.py
│
├── frontend/
│
├── datasets/
│
├── evaluation/
│
├── tests/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
└── .env.example
```

---

## ⚙ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/hybrid-token-efficient-routing-agent.git

cd hybrid-token-efficient-routing-agent
```

Install Python dependencies

```bash
pip install -r requirements.txt
```

Create environment file

```bash
cp .env.example .env
```

Run Backend

```bash
python -m uvicorn app.main:app --reload
```

Run Frontend

```bash
cd frontend

npm install

npm run dev
```

---

## 🔐 Environment Variables

```
FIREWORKS_API_KEY=your_api_key

FIREWORKS_BASE_URL=https://api.fireworks.ai/inference/v1

DEFAULT_MODEL=accounts/fireworks/models/gpt-oss-120b

CONFIDENCE_THRESHOLD=0.85
```

---

## 🌐 REST API

### POST /route

Request

```json
{
  "prompt": "Explain Quantum Computing"
}
```

Response

```json
{
  "model": "accounts/fireworks/models/gpt-oss-120b",
  "task": "general",
  "complexity": 3,
  "confidence": 0.94,
  "tokens": 210,
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

Analyze token usage

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

## 📷 Demo

<img width="100%" src="images/demo.png">

---

## 🚀 Future Improvements

- Streaming responses
- Multi-provider routing
- RAG support
- GPU utilization dashboard
- Real-time cost estimation
- Multi-agent orchestration

---

## 🏆 AMD Developer Hackathon 2026

**Track 1 – Hybrid Token-Efficient Routing Agent**

Built using:

- AMD Infrastructure
- Fireworks AI
- GPT-OSS-120B
- FastAPI
- React
- TypeScript

---

## 📄 License

MIT License

---

**Made with ❤️ for the AMD Developer Hackathon 2026**
