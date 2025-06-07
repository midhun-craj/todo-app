from fastapi import APIRouter, Depends, Query
import logging
from sqlalchemy.orm import Session
from typing import Optional

from app.schemas.todo_schema import TodoCreate, TodoOut
from app.services import todo_service
from app.db.session import get_db

router = APIRouter(prefix="/todo", tags=["Todo"])

@router.post("/", response_model=TodoOut)
def create_todo(todo: TodoCreate, db: Session = Depends(get_db)):
    logging.info("Reached the todo create endpoint.")
    res = todo_service.create_todo(todo, db)
    logging.info(f"Result type: {type(res)}, content: {res}")
    return res

# @router.get("/", response_model=list[TodoOut])
# def get_todos(db: Session = Depends(get_db)):
#     logging.info("Reached the get todo endpoint.")
#     res = todo_service.get_todos(db)
#     logging.info(f"Result type: {type(res)}, content: {res}")
#     return res

@router.get("/filter", response_model=list[TodoOut])
def filter_todos(search: Optional[str] = Query(None), 
                skip: int = Query(0), 
                limit: int = Query(10), 
                db: Session = Depends(get_db)):
    logging.info("Reached the todo filter endpoint.")
    res = todo_service.get_filtered_todos(search, skip, limit, db)
    logging.info(f"Result type: {type(res)}, content: {res}")
    return res