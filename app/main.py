from fastapi import FastAPI

from app.routers import servicos


app = FastAPI(title = "Service Monitor API", version = "0.1.0")
app.include_router(servicos.router)

@app.get("/health")
def health():
    return { "status": "ok"}