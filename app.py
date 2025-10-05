from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

# Autoriser CORS (ton frontend pourra appeler le backend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # tu pourras remplacer "*" par ton vrai domaine frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Backend Zoubir is running 🚀"}

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    user_message = data.get("message", "")
    # pour le moment on fait simple :
    return {"reply": f"Tu as dit: {user_message}"}
