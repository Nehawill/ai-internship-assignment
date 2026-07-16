from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.parser.pdf_reader import open_pdf, build_sections
from app.services.document_service import save_sections

from app.database import SessionLocal
from app.models.document import DocumentSection
from app.comparison.version_compare import compare_versions

router = APIRouter(
    prefix="/documents",
    tags=["Documents"]
)
class IngestRequest(BaseModel):
    pdf_path: str
    version: str

#end points
@router.get("/compare/{version1}/{version2}")
def compare_documents(version1: str, version2: str):

    db = SessionLocal()

    try:
        v1_sections = db.query(DocumentSection).filter_by(version=version1).all()
        v2_sections = db.query(DocumentSection).filter_by(version=version2).all()

        return compare_versions(v1_sections, v2_sections)

    finally:
        db.close()
@router.post("/ingest")
def ingest_document(request: IngestRequest):

    try:
        pdf = open_pdf(request.pdf_path)

        sections = build_sections(pdf)

        save_sections(sections, request.version)

        return {
            "message": f"{request.version} ingested successfully!",
            "sections": len(sections)
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
