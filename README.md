# LLM CI/CD Log Analyzer

An AI-powered DevOps tool that analyzes CI/CD and application logs
to detect failures, explain root causes, and suggest fixes using LLMs.

## Features
- Upload Jenkins / CI logs
- Extract error lines
- LLM-based root cause analysis
- Step-by-step fix suggestions

## Tech Stack
- Python
- FastAPI
- OpenAI LLM
- Docker

## Run Locally
```bash
export OPENAI_API_KEY=your_key
pip install -r requirements.txt
uvicorn app.main:app --reload
