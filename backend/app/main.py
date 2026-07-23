from fastapi import FastAPI
from backend.app.api.V1.auth import router as auth_router
from backend.app.api.V1.documents import router as document_router

app = FastAPI(
    title="Workforce AI",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to WorkForce AI"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

app.include_router(auth_router)
app.include_router(document_router)