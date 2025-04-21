from pydantic import BaseModel, Field
from datetime import datetime


class FolderCreate(BaseModel):
    """
    Схема для создания новой папки
    """
    user_id: int = Field(..., example=1)
    name: str = Field(..., example="MyFolder")


class FolderRead(BaseModel):
    """
    Отображение информации о папке (в ответе)
    """
    folder_id: int
    user_id: int
    name: str
    created_at: datetime

    class Config:
        from_attributes = True  # pydantic 2.x (или orm_mode=True для 1.x)


class FolderUpdate(BaseModel):
    """
    Для обновления папки (например, переименование)
    """
    name: str = Field(..., example="RenamedFolder")
