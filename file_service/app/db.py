from typing import Dict
from app.models import FileRecord

"""
Храним файлы (их метаданные и контент) в памяти:
   file_id -> FileRecord
"""

fake_files_db: Dict[int, FileRecord] = {}
fake_file_id_seq = 0


def get_next_file_id() -> int:
    global fake_file_id_seq
    fake_file_id_seq += 1
    return fake_file_id_seq
