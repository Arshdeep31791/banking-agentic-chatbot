from fastapi import FastAPI
from crew.banking_crew import crew

app = FastAPI()

@app.post("/chat")
def chat(query: str):
    result = crew.kickoff(inputs={"query": query})
    return {"response": result}
