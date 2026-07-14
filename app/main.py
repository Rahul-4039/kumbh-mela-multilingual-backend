from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.models.chat_models import ChatRequest, ChatResponse
from app.services.llm_service import LLMService

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "message": "Enterprise AI Backend Running 🚀"
    }


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    answer = LLMService.ask(request.message)

    return ChatResponse(
        responseText=answer
    )