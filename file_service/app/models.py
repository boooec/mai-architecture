from datetime import datetime


class FileRecord:
    """
    Модель файла (упрощённая).
    file_id: уникальный идентификатор (str)
    folder_id: в какой папке лежит (int)
    filename: имя файла (str)
    content: содержимое (bytes) — в реальном проекте вместо этого можно хранить путь к объекту в S3, MinIO и т.д.
    created_at: время создания (datetime)
    """

    def __init__(self, file_id: str, folder_id: int, filename: str, content: bytes, created_at: datetime):
        self.file_id = file_id
        self.folder_id = folder_id
        self.filename = filename
        self.content = content
        self.created_at = created_at

    def dict(self) -> dict:
        return {
            "file_id": self.file_id,
            "folder_id": self.folder_id,
            "filename": self.filename,
            "content": self.content,
            "created_at": self.created_at.isoformat()
        }
