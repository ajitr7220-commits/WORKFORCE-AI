from fastapi import FastAPI

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