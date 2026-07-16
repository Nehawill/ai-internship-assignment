from app.database import SessionLocal
from app.models.document import DocumentSection

from app.comparison.version_compare import compare_versions

db = SessionLocal()

v1 = db.query(DocumentSection).filter_by(version="v1").all()
v2 = db.query(DocumentSection).filter_by(version="v2").all()

results = compare_versions(v1, v2)

for result in results:
    print(result)

db.close()