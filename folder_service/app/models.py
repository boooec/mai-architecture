from datetime import datetime


class Folder:
    """
    Доменная модель для папки.
    folder_id: int - уникальный ID
    user_id: int   - ID пользователя, которому принадлежит папка
    name: str      - название папки (например, 'Documents')
    created_at: datetime - время создания
    """

    def __init__(self, folder_id: int, user_id: int, name: str, created_at: datetime):
        self.folder_id = folder_id
        self.user_id = user_id
        self.name = name
        self.created_at = created_at

    def dict(self) -> dict:
        return {
            "folder_id": self.folder_id,
            "user_id": self.user_id,
            "name": self.name,
            "created_at": self.created_at.isoformat()
        }
