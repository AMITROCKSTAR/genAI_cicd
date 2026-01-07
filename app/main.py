from fastapi import FastAPI
from pydantic import BaseModel
from app.chain import ask_llm

app = FastAPI()

class Query(BaseModel):
    question:str


@app.get("/")
def health():
    return {"status":"++++++++ Positive response +++++"}

@app.post("/ask")

def ask(query:Query):
    answer = ask_llm(query.question)
    return {"answer": answer}