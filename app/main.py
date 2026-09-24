from fastapi import FastAPI
from app.routes import router as products_router

app = FastAPI(title="QA API Test Platform")

app.include_router(products_router)


@app.get("/")
def root():
    return {"message": "QA API Test Platform is running"}


@app.get("/health")
def health():
    return {"status": "healthy"}
