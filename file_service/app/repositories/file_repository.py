from typing import Optional, List
from datetime import datetime
from app.models import FileRecord
from app.db import fake_files_db, get_next_file_id


class FileRepository:
    @staticmethod
    def create_file(folder_id: int, filename: str, content: bytes) -> FileRecord:
        new_id = get_next_file_id()
        file_record = FileRecord(
            file_id=new_id,
            folder_id=folder_id,
            filename=filename,
            content=content,
            created_at=datetime.utcnow()
        )
        fake_files_db[new_id] = file_record
        return file_record

    @staticmethod
    def get_file_by_id(file_id: int) -> Optional[FileRecord]:
        return fake_files_db.get(file_id)

    @staticmethod
    def list_files() -> List[FileRecord]:
        return list(fake_files_db.values())

    @staticmethod
    def delete_file(file_id: int) -> bool:
        if file_id in fake_files_db:
            del fake_files_db[file_id]
            return True
        return False
