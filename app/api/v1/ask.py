from fastapi import APIRouter

from app.schema.requests import AskRequest
from app.schema.responses import AskResponse
from app.services.sql_service import SQLService
from app.tools.database_tool import DatabaseTool

router = APIRouter()


@router.post("/ask", response_model=AskResponse)
def ask_question(request: AskRequest):

    sql_query = SQLService.generate_sql(
        request.question
    )

    result = DatabaseTool.execute_query(
        sql_query
    )

    return AskResponse(
        question=request.question,
        sql=sql_query,
        result=result,
    )
