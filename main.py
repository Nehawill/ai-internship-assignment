from fastapi import FastAPI
from app.api.document_api import router as document_router

app = FastAPI(
    title="Tri9T AI Engineering Assignment",
    version="1.0.0"
)
app.include_router(document_router)

@app.get("/")
def root():
    return {
        "message": "Welcome to the Tri9T AI Engineering Assignment API!"
    }