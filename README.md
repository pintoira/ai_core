# ai_core

A Python-based AI bot starter project that includes:
- chatbot interface
- coding assistant capabilities
- task automation workflows
- FastAPI backend for integration
- OpenAI-compatible LLM support

## Features

- Chat endpoint for conversational responses
- Code assistant for coding help, debugging, and refactors
- Task automation endpoint for planning and execution guidance
- Environment-based configuration
- Ready for extension with real tools, memory, and database integrations

## Stack

- Python 3.11+
- FastAPI
- Pydantic
- httpx
- OpenAI SDK

## Quick start

1. Create a virtual environment
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

2. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

3. Configure environment
   ```bash
   cp .env.example .env
   ```

4. Start the app
   ```bash
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

## API examples

### Chat

```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"message":"Hello!","context":"General conversation"}'
```

### Code assistant

```bash
curl -X POST http://localhost:8000/assistant \
  -H "Content-Type: application/json" \
  -d '{"prompt":"Explain how to build a Flask app that uses SQLite."}'
```

### Task automation

```bash
curl -X POST http://localhost:8000/task \
  -H "Content-Type: application/json" \
  -d '{"task":"Create a Python script to fetch weather data and save it to CSV."}'
```

## Environment variables

See `.env.example` for configuration values.

## Notes

This is a starter implementation designed to be expanded into a production AI assistant with:
- memory and conversation history
- tool calling and workflow execution
- database-backed task tracking
- authentication and authorization
- deployment to cloud platforms
