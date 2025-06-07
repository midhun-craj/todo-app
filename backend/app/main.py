from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import todo_routes
from app.db.base import Base
from app.db.session import engine

# Create all tables.
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Allow CORS for the frontend.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(todo_routes.router)