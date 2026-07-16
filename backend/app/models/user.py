from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from backend.app.db.database import Base

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)

    organization_id: Mapped[int] = mapped_column(
        ForeignKey("organizations.id")
    )

    name: Mapped[str] = mapped_column(String(255))

    email: Mapped[str] = mapped_column(
        String(255),
        unique=True
    )

    password_hash: Mapped[str] = mapped_column(String(255))

    role: Mapped[str] = mapped_column(default="admin")