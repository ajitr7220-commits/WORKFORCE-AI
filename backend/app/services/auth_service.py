from sqlalchemy.orm import Session

from backend.app.models.user import User
from backend.app.models.organization import Organization
from backend.app.schemas.auth import RegisterRequest
from backend.app.auth.password import hash_password
from backend.app.auth.jwt import create_access_token
from backend.app.auth.password import verify_password


class AuthService:

    @staticmethod
    def register(db: Session, request: RegisterRequest):

        # Check if email already exists
        existing_user = db.query(User).filter(
            User.email == request.email
        ).first()

        if existing_user:
            raise ValueError("Email already registered")

        # Create organization
        organization = Organization(
            name=request.organization_name
        )

        db.add(organization)
        db.flush()

        # Create admin user
        user = User(
            organization_id=organization.id,
            name=request.name,
            email=request.email,
            password_hash=hash_password(request.password),
            role="admin"
        )

        db.add(user)
        db.commit()
        db.refresh(user)

        return user
    
    @staticmethod
    def login(db:Session, email:str, password:str):

        user = db.query(User).filter(User.email == email).first()
        if not user:
            raise ValueError("INvalid email and password")
        
        if not verify_password(password,user.password_hash):
            raise ValueError ("Invalid email or password")
        token = create_access_token(
            {
                "sub": user.email
            }
        )

        return {
            "access_token": token,
            "token_type": "bearer"
        }
