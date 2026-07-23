from pathlib import Path
import shutil

from fastapi import APIRouter, Depends, File, UploadFile
from sqlalchemy.orm import Session

from backend.app.auth.jwt import get_current_user
from backend.app.db.database import get_db
from backend.app.models.user import User
from backend.app.services.document_service import DocumentService

router = APIRouter(
    prefix="/documents",
    tags=["Documents"]
)

UPLOAD_DIR = "uploads"
Path(UPLOAD_DIR).mkdir(exist_ok=True)


@router.post("/upload")
def upload_document(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    file_path = f"{UPLOAD_DIR}/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    document = DocumentService.create_document(
        db=db,
        organization_id=current_user.organization_id,
        filename=file.filename,
        file_path=file_path
    )

    return {
        "message": "Document uploaded successfully",
        "document_id": document.id,
        "filename": document.filename
    }
