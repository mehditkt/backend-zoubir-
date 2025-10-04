from fastapi import FastAPI
from pydantic import BaseModel
import requests
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

# Autoriser ton site frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # remplace par ton domaine si tu veux
    allow_methods=["*"],
    allow_headers=["*"],
)

HF_TOKEN = os.environ.get("HF_TOKEN")  # Ton token Hugging Face caché
API_URL = "https://api-inference.huggingface.co/models/TonPseudo/zoubir-ia"  # remplace par ton modèle exact

class Message(BaseModel):
    inputs: str

@app.post("/chat")
def chat(msg: Message):
    headers = {"Authorization": f"Bearer {HF_TOKEN}"}
    response = requests.post(API_URL, headers=headers, json={"inputs": msg.inputs})
    return response.json()
