# app.py
from fastapi import FastAPI
from pydantic import BaseModel
import os

app = FastAPI()

# 模擬一個簡單模型：判斷文字裡面有沒有 "hello"
class TextIn(BaseModel):
    text: str

@app.post("/predict")
def predict(input: TextIn):
    if "hello" in input.text.lower():
        return {"label": "greeting"}
    else:
        return {"label": "other"}

# Add a root endpoint for testing
@app.get("/")
def root():
    return {"message": "Welcome to the AI prediction API!"}

# # Automatic API docs
# @app.get("/docs")
# def docs():
#     return {"redirect": "/docs"}

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)

