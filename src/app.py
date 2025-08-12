# app.py
from fastapi import FastAPI
from pydantic import BaseModel

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
