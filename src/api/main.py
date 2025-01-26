from typing import List
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from fastapi import FastAPI, HTTPException, Depends
from src.api.schema import Flashcard, Hello
from src.api.dependencies import JSONDatabase
from src.api.routes import router

def get_database():
    return JSONDatabase()


app = FastAPI(
    title="Flashcard AI Backend",
    description="Simple Flashcard Management System",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust origins as needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(router)