from sqlalchemy.orm import Session

from backend.app.models.document import Document


class DocumentService:

    @staticmethod
    def create_document(
        db: Session,
        organization_id: int,
        filename: str,
        file_path: str
    ):

        document = Document(
            organization_id=organization_id,
            filename=filename,
            file_path=file_path
        )

        db.add(document)
        db.commit()
        db.refresh(document)

        return document