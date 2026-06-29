
from fastapi import FastAPI
from routes.medicine_routes import router

app = FastAPI(title="AI Pharma Assistant")

app.include_router(router)

@app.get("/")
def home():
    return {"message": "AI Pharma Assistant Running"}
