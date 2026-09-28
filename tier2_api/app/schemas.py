"""Pydantic request/response models"""

from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

# User schemas
class UserCreate(BaseModel):
    email: str
    username: str
    password: str

class UserResponse(BaseModel):
    id: str
    email: str
    username: str
    created_at: datetime
    
    class Config:
        from_attributes = True

# Chat schemas
class ChatRequest(BaseModel):
    query: str
    conversation_id: Optional[str] = None

class ChatResponse(BaseModel):
    id: str
    query: str
    response: str
    sources: List[str] = []
    created_at: datetime
    
    class Config:
        from_attributes = True

# Document schemas
class DocumentUpload(BaseModel):
    filename: str
    content: str

class DocumentResponse(BaseModel):
    id: str
    filename: str
    size: int
    created_at: datetime
    
    class Config:
        from_attributes = True