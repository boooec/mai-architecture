from fastapi import APIRouter, Depends, HTTPException
from typing import List
from app.schemas import FileCreate, FileRead, FileContent
from app.services.file_service import FileService
from app.repositories.file_repository import FileRepository
from app.auth import verify_token


router = APIRouter(prefix="/files", tags=["files"])
service = FileService(FileRepository())


@router.post("", response_model=FileRead)
def upload_file(payload: FileCreate, token_user: str = Depends(verify_token)):
    file_record = service.upload_file(payload.folder_id, payload.filename, payload.content)
    return file_record.dict()


@router.get("", response_model=List[FileRead])
def list_all_files(token_user: str = Depends(verify_token)):
    files = service.list_files()
    return [f.dict() for f in files]


@router.get("/{file_id}", response_model=FileRead)
def get_file_metadata(file_id: int, token_user: str = Depends(verify_token)):
    file_record = service.get_file(file_id)
    if not file_record:
        raise HTTPException(status_code=404, detail="File not found")
    return file_record.dict()


@router.get("/{file_id}/content", response_model=FileContent)
def get_file_content(file_id: int, token_user: str = Depends(verify_token)):
    """
    Получить содержимое файла (bytes -> str).
    """
    file_record = service.get_file(file_id)
    if not file_record:
        raise HTTPException(status_code=404, detail="File not found")
    # Преобразуем bytes в str (utf-8)
    return {"content": file_record.content.decode("utf-8")}


@router.delete("/{file_id}")
def delete_file(file_id: int, token_user: str = Depends(verify_token)):
    success = service.delete_file(file_id)
    if not success:
        raise HTTPException(status_code=404, detail="File not found")
    return {"detail": "File deleted"}
