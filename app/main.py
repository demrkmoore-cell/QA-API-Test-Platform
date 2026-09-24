from fastapi import FastAPI
from app.routes import router as products_router
from app.ui_routes import router as ui_router

app = FastAPI(title="QA API Test Platform")

app.include_router(products_router)
app.include_router(ui_router)


@app.get("/")
def root():
    return {"message": "QA API Test Platform is running"}


@app.get("/health")
def health():
    return {"status": "healthy"}
