from fastapi import HTTPException
from sqlalchemy.orm import Session
from typing import Optional

from app.crud import todo_crud
from app.schemas.todo_schema import TodoCreate

def create_todo(todo_data: TodoCreate, db: Session):
    try: 
        return todo_crud.create_todo(todo_data, db)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error creating todo.\n{str(e)}")

def get_todos(db: Session):
    try:
        return todo_crud.get_todos(db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching todo's.\n{str(e)}")
    
def get_filtered_todos(search: Optional[str], skip: int, limit: int, db: Session):
    try:
        return todo_crud.get_filtered_todos(search, skip, limit, db)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error fetching filtered todos.\n{str(e)}")