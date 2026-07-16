from app.database import SessionLocal
from app.models.document import DocumentSection

db = SessionLocal()

sections = db.query(DocumentSection).all()

print(f"Total Sections: {len(sections)}\n")

for section in sections:
    print("=" * 60)
    print(f"ID    : {section.id}")
    print(f"Title : {section.title}")
    print(f"Level : {section.level}")
    print(f"Page  : {section.page}")
    print(f"Content Preview: {section.content[:100]}")

db.close()