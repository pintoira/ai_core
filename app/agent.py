from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from app.config import settings
from app.agent import AIChatBot

app = FastAPI(title="ai_core", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

bot = AIChatBot(api_key=settings.openai_api_key, model_name=settings.model_name)


class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1)
    context: str = ""


class CodeRequest(BaseModel):
    prompt: str = Field(..., min_length=1)
    repo_context: str = ""


class TaskRequest(BaseModel):
    task: str = Field(..., min_length=1)


@app.get("/health")
def health() -> dict:
    return {"status": "ok", "service": "ai_core"}


@app.post("/chat")
def chat(request: ChatRequest) -> dict:
    response = bot.chat(request.message, request.context)
    return {"response": response}


@app.post("/assistant")
def code_assistant(request: CodeRequest) -> dict:
    response = bot.code_assist(request.prompt, request.repo_context)
    return {"response": response}


@app.post("/task")
def task(request: TaskRequest) -> dict:
    response = bot.automate_task(request.task)
    return {"response": response}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", host=settings.app_host, port=settings.app_port, reload=True)
