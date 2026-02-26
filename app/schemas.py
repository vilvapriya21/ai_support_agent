from pydantic import BaseModel
from typing import Literal


class AskRequest(BaseModel):
    user_id: str
    message: str


class AskResponse(BaseModel):
    type: Literal["answer", "clarification", "out_of_scope"]
    message: str
