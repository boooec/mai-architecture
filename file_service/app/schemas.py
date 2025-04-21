from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class FileCreate(BaseModel):
    """
    Схема для запроса при загрузке файла.
    folder_id – в какую папку (int),
    filename – имя файла (str),
    content – содержимое (base64 или что-то упрощённое).
    """
    folder_id: int = Field(..., example=1)
    filename: str = Field(..., example="image.png")
    # Упрощённо: пусть content – обычная строка, которую мы потом преобразуем в bytes
    content: Optional[str] = Field(default=None, example="base64-encoded content")


class FileRead(BaseModel):
    """
    Возвращаем базовые метаданные файла (без контента).
    """
    file_id: int
    folder_id: int
    filename: str
    created_at: datetime

    class Config:
        from_attributes = True


class FileContent(BaseModel):
    """
    Возвращаем само содержимое файла (при GET /files/{file_id}/content)
    """
    content: str
