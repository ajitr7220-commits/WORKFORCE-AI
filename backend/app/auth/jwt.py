from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt
from backend.app.core.config import settings
from fastapi import  Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import session
from backend.app.db.database import get_db
from backend.app.models.user import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/auth/login')



def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    to_encode.update({"exp": expire})

    return jwt.encode(
        to_encode,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )

def decode_access_token(token: str):
    try: 
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )

        return payload
    except JWTError:
        return None
    
def get_current_user(
        token: str = Depends(oauth2_scheme),
        db: session = Depends(get_db)
):
    payload = decode_access_token(token)

    if payload is None:
        raise HTTPException(
            status_code=401,
            detail="Invaild token"
        )   
    
    email = payload.get("sub")
    user = db.query(User).filter(
        User.email == email
    ).first()

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="User not found"
        )
    
    return user



