from app.database import Base, engine
from app.models.document import DocumentSection

Base.metadata.create_all(bind=engine)

print("Database created successfully!")