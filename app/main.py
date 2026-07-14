import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.models.chat_models import ChatRequest, ChatResponse
from app.services.llm_service import LLMService
from app.services.tts_service import TTSService

app = FastAPI()

os.makedirs("app/audio", exist_ok=True)

app.mount(
    "/audio",
    StaticFiles(directory="app/audio"),
    name="audio",
)

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

    result = LLMService.ask(request.message)

    audio_file = TTSService.generate_speech(
    result["answer"],
    result["language"]
)

    return ChatResponse(
    responseText=result["answer"],
    audioUrl=f"http://192.168.2.97:8000/audio/{audio_file}"
)