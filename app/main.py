from fastapi import FastAPI

app = FastAPI(title="QA API Test Platform")


@app.get("/")
def root():
    return {"message": "QA API Test Platform is running"}


@app.get("/health")
def health():
    return {"status": "healthy"}
