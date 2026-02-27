from fastapi import FastAPI
from app.schemas import AskRequest, AskResponse
from app.agent import Agent
from app.core.logging_config import setup_logging

setup_logging()

app = FastAPI()
agent = Agent()


@app.post("/ask", response_model=AskResponse)
def ask(request: AskRequest):
    return agent.handle_message(
        user_id=request.user_id,
        message=request.message
    )
