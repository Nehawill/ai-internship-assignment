from fastapi import FastAPI

app = FastAPI(
    title="Tri9T AI Engineering Assignment",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "Welcome to the Tri9T AI Engineering Assignment API!"
    }