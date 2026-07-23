from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from backend. app.db.database import Base


class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    organization_id = Column(
        Integer,
        ForeignKey("organizations.id"),
        nullable=False
    )
    filename = Column(String, nullable=False)
    file_path = Column(String, nullable=False)

    organization = relationship(
        "Organization",
        back_populates="documents"
    )