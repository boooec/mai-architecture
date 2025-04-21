from typing import List
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

    def upload_file(self, folder_id: int, filename: str, content_str: str | None) -> FileRecord:
        # Если content_str не задан, пусть будет пустое содержимое
        content_bytes = content_str.encode("utf-8") if content_str else b""
        return self.repo.create_file(folder_id, filename, content_bytes)

    def list_files(self) -> List[FileRecord]:
        return self.repo.list_files()

    def get_file(self, file_id: int) -> FileRecord | None:
        return self.repo.get_file_by_id(file_id)

    def delete_file(self, file_id: int) -> bool:
        return self.repo.delete_file(file_id)
