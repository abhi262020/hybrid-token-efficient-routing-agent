# 🚀 Hybrid Token-Efficient Routing Agent

AMD Developer Hackathon 2026 – Track 1

---

## Overview

Hybrid Token-Efficient Routing Agent intelligently selects the best LLM for a prompt based on task type, complexity, confidence, and token efficiency.

Instead of sending every request to the largest model, it dynamically routes prompts to lightweight or powerful models as needed, reducing latency, API costs, and token usage.

---

## Features

- Automatic prompt classification
- Complexity estimation
- Intelligent model routing
- Confidence scoring
- Automatic escalation
- Token usage tracking
- FastAPI backend
- React + Vite frontend
- Fireworks AI integration

---

## Models

- Llama 3.1 8B
- Qwen3 30B
- DeepSeek V3

---

## Tech Stack

### Backend

- Python
- FastAPI
- Fireworks AI API
- HTTPX

### Frontend

- React
- TypeScript
- Vite

---

## Installation

Clone the repository

```bash
git clone https://github.com/yourusername/hybrid-router.git

cd hybrid-router
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create environment file

```bash
cp .env.example .env
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

## API

POST

```
/route
```

Example

```json
{
    "prompt":"Explain Quantum Computing"
}
```

Response

```json
{
    "model":"llama-v3.1-8b",
    "task":"general",
    "complexity":0.42,
    "confidence":0.95,
    "tokens":210,
    "response":"..."
}
```

---

## Evaluation

```bash
python evaluation/benchmark.py
```

```bash
python evaluation/compare_models.py
```

```bash
python evaluation/token_analysis.py
```

---

## Testing

```bash
pytest
```

---

## Docker

Build

```bash
docker compose up --build
```

---

## License

MIT