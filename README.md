# 🤖 AI RAG Chatbot

> Production-grade Retrieval-Augmented Generation Chatbot with FastAPI Backend

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

## 🎯 Projects

### Tier 1: RAG Chatbot MVP ✅
- LangChain + OpenAI integration
- Document processing
- Retrieval pipeline
- Test coverage: 80%+

### Tier 2: FastAPI Backend 🚀 
- REST API with 5+ endpoints
- SQLite database
- User authentication (JWT)
- Production-ready deployment

## 🚀 Quick Start

```bash
# Clone repo
git clone https://github.com/konavibha-ship-it/ai-rag-chatbot.git
cd ai-rag-chatbot

# Create venv
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run Tier 1
python -m src.main

# Run Tier 2 API
cd tier2_api
python -m app.main
```

## 📚 Projects

### Tier 1: RAG Chatbot
```bash
cd ai-rag-chatbot
python -m src.main
```

### Tier 2: FastAPI Backend
```bash
cd tier2_api
python -m uvicorn app.main:app --reload
# Visit: http://localhost:8000/docs
```

## 🛠️ Tech Stack

**Tier 1:**
- Python, LangChain, OpenAI, Pinecone

**Tier 2:**
- FastAPI, SQLAlchemy, SQLite, Pydantic

## 📊 Features

✅ Document retrieval and processing
✅ LLM-powered responses
✅ Chat history storage
✅ User authentication
✅ REST API with Swagger docs
✅ Docker-ready
✅ 80%+ test coverage

## 🧪 Tests

```bash
# Tier 1
pytest tests/ -v --cov=src

# Tier 2
pytest tier2_api/tests/ -v --cov=app
```

## 📄 License

MIT License - see LICENSE for details

---

**Built by:** @konavibha-ship-it
**Status:** In Development (Tier 2 Active)