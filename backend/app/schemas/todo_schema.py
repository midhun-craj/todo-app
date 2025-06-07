from pydantic import BaseModel, ConfigDict

class TodoCreate(BaseModel):
    title: str

class TodoOut(BaseModel):
    id: int
    title: str
    
    model_config = ConfigDict(from_attributes=True)