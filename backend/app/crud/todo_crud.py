from sqlalchemy.orm import Session
import logging
from typing import Optional
from app.schemas.todo_schema import TodoCreate, TodoOut
from app.models.todo_model import Todo

def create_todo(todo_data: TodoCreate, db: Session) -> TodoOut:
    new_todo = Todo(title=todo_data.title)
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    logging.info(f"Todo created: {new_todo}")
    return new_todo

def get_todos(db: Session) -> list[TodoOut]:
    data = db.query(Todo).all()
    logging.info(f"Todo data: {data}")
    return data

def get_filtered_todos(search: Optional[str], skip: int, limit: int, db: Session) -> list[TodoOut]:
    query = db.query(Todo)
    if search:
        query = query.filter(Todo.title.ilike(f"%{search}%"))
    logging.info(f"Performing wildcard search.")
    return query.offset(skip).limit(limit).all()