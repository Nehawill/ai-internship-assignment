from sqlalchemy import Column, Integer, String, Text

from app.database import Base


class DocumentSection(Base):
    __tablename__ = "document_sections"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    level = Column(Integer, nullable=False)
    page = Column(Integer, nullable=False)
    content = Column(Text, nullable=False)