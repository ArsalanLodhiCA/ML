from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

pipe = pipeline('translation','./model/t5-base') 

app = FastAPI()

class TexttoTranslate(BaseModel):
    input_text: str

@app.get("/")
def index():
    return {"message": "Hello World"}

@app.get("/cool")
def cool_stuff():
    return {"message" : "This is neat"}

@app.get("/ping")
def ping():
    return {"message": "pong"}

@app.post("/echo")
def echo(text_to_translate: TexttoTranslate):
    return {"message": text_to_translate.input_text}

@app.post("/translate")
def translate(text_to_translate: TexttoTranslate):
    return {"translation": pipe(text_to_translate.input_text)}

    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)