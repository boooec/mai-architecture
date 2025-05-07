from typing import List, Optional
from datetime import datetime
from app.models import FileRecord
from app.repositories.file_repository import FileRepository


class FileService:
    """
    Логика управления файлами.
    Здесь можно вызвать FolderService для проверки: существует ли указанная папка?
    Пока что пропускаем эту проверку.
    """

    def __init__(self, repo: FileRepository):
        self.repo = repo

    async def upload_file(self, folder_id: int, filename: str, content_str: str | None) -> FileRecord:
        # Если content_str не задан, пусть будет пустое содержимое
        content_bytes = content_str.encode("utf-8") if content_str else b""
        return await self.repo.create_file(folder_id, filename, content_bytes, created_at=datetime.now())

    async def list_files(self) -> List[FileRecord]:
        return await self.repo.list_files()

    async def find_files(self, file_id: Optional[str] = None, folder_id: Optional[str] = None, filename: Optional[str] = None) -> List[FileRecord]:
        return await self.repo.find_files(file_id, folder_id, filename)

    async def get_file(self, file_id: str) -> FileRecord | None:
        return await self.repo.get_file_by_id(file_id)

    async def delete_file(self, file_id: str) -> bool:
        return await self.repo.delete_file(file_id)
