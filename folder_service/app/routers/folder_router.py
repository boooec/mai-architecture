from fastapi import APIRouter, Depends, HTTPException
from typing import List
from app.schemas import FolderCreate, FolderRead, FolderUpdate
from app.services.folder_service import FolderService
from app.repositories.folder_repository import FolderRepository
from app.auth import verify_token

router = APIRouter(prefix="/folders", tags=["folders"])
service = FolderService(FolderRepository())


@router.post("", response_model=FolderRead)
def create_folder(payload: FolderCreate, token_user: str = Depends(verify_token)):
    """
    Создать новую папку
    """
    folder = service.create_folder(payload.user_id, payload.name)
    return folder.dict()


@router.get("", response_model=List[FolderRead])
def list_all_folders(token_user: str = Depends(verify_token)):
    """
    Получить список всех папок (без фильтрации по user_id).
    """
    folders = service.list_folders()
    return [f.dict() for f in folders]


@router.get("/{folder_id}", response_model=FolderRead)
def get_folder_by_id(folder_id: int, token_user: str = Depends(verify_token)):
    """
    Получить папку по ID
    """
    folder = service.get_folder(folder_id)
    if not folder:
        raise HTTPException(status_code=404, detail="Folder not found")
    return folder.dict()


@router.patch("/{folder_id}", response_model=FolderRead)
def update_folder(folder_id: int, payload: FolderUpdate, token_user: str = Depends(verify_token)):
    """
    Переименовать папку
    """
    try:
        folder = service.update_folder(folder_id, payload.name)
        return folder.dict()
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.delete("/{folder_id}")
def delete_folder(folder_id: int, token_user: str = Depends(verify_token)):
    """
    Удалить папку по ID
    """
    success = service.delete_folder(folder_id)
    if not success:
        raise HTTPException(status_code=404, detail="Folder not found")
    return {"detail": "Folder deleted"}
