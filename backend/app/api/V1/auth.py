from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

from backend.app.db.database import get_db
from backend.app.schemas.auth import RegisterRequest
from backend.app.schemas.auth import LoginRequest
from backend.app.services.auth_service import AuthService
from backend.app.auth.jwt import get_current_user
from backend.app.models.user import User

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/register")
def register(
    request: RegisterRequest,
    db: Session = Depends(get_db)
):
    try:
        user = AuthService.register(db, request)

        return {
            "message": "Registration successful",
            "user_id": user.id,
            "organization_id": user.organization_id
        }

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )



@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    try:
        return AuthService.login(
            db,
            form_data.username,
            form_data.password
        )
    except ValueError as e:
        raise HTTPException(
            status_code=401,
            detail=str(e)
        )
    
@router.get("/me")
def me(current_user: User = Depends(get_current_user)):
    return current_user
