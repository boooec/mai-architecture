from typing import List, Optional
from bson import ObjectId
from datetime import datetime

from app.models import FileRecord
from app.db import db


class FileRepository:
    collection = db.files

    @staticmethod
    async def create_file(folder_id: str, filename: str, content: str, created_at: datetime) -> FileRecord:
        doc = {"folder_id": folder_id, "filename": filename, "content": content, "created_at": created_at}
        result = await FileRepository.collection.insert_one(doc)
        return FileRecord(file_id=str(result.inserted_id), folder_id=folder_id, filename=filename, content=content, created_at=created_at)

    @staticmethod
    async def get_file_by_id(file_id: str) -> Optional[FileRecord]:
        doc = await FileRepository.collection.find_one({"_id": ObjectId(file_id)})
        if not doc:
            return None
        return FileRecord(file_id=str(doc["_id"]), folder_id=doc["folder_id"], filename=doc["filename"], content=doc["content"], created_at=doc["created_at"])

    @staticmethod
    async def list_files() -> List[FileRecord]:
        files: List[FileRecord] = []
        async for doc in FileRepository.collection.find():
            files.append(FileRecord(
                file_id=str(doc["_id"]), folder_id=doc["folder_id"], filename=doc["filename"], content=doc["content"], created_at=doc["created_at"]
            ))
        return files

    @staticmethod
    async def find_files(file_id: Optional[str] = None, folder_id: Optional[str] = None, filename: Optional[str] = None) -> List[FileRecord]:
        query: dict = {}
        if file_id:
            query["file_id"] = file_id
        if folder_id:
            query["folder_id"] = folder_id
        if filename:
            query["filename"] = filename
        files: List[FileRecord] = []
        async for doc in FileRepository.collection.find(query):
            files.append(FileRecord(
                file_id=str(doc["_id"]), folder_id=doc["folder_id"], filename=doc["filename"], content=doc["content"], created_at=doc["created_at"]
            ))
        return files

    @staticmethod
    async def delete_file(file_id: str) -> bool:
        result = await FileRepository.collection.delete_one({"_id": ObjectId(file_id)})
        return result.deleted_count == 1
