from fastapi import FastAPI
from app.schemas import AskRequest
from app.agent import Agent

app = FastAPI()
agent = Agent()


@app.post("/ask")
def ask(request: AskRequest):
    response = agent.handle_message(
        user_id=request.user_id,
        message=request.message
    )
    return {"reply": response}
