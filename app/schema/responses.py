from pydantic import BaseModel


class AskResponse(BaseModel):
    question: str
    sql: str
    result: list
