from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from backend.app.db.database import Base

class Organization(Base):
    __tablename__ = "organizations"

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(String(255))

    plan: Mapped[str] = mapped_column(String(50), default="free")