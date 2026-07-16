from app.database import SessionLocal
from app.models.document import DocumentSection


def save_sections(sections):
    """
    Save parsed document sections into the database.
    """

    db = SessionLocal()

    try:

        for section in sections:

            document = DocumentSection(
                title=section["title"],
                level=section["level"],
                page=section["page"],
                content="\n".join(section["content"])
            )

            db.add(document)

        db.commit()

    finally:
        db.close()