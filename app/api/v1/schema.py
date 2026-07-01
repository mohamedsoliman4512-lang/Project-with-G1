from fastapi import APIRouter

from app.tools.schema_tool import SchemaTool

router = APIRouter()


@router.get("/schema")
def get_schema():

    tables = SchemaTool.get_tables()

    return {
        "tables": tables
    }


@router.get("/schema/details/{table_name}")
def get_table_details(table_name: str):

    columns = SchemaTool.get_columns(
        table_name
    )

    return {
        "table": table_name,
        "columns": columns
    }
