from app.prompts.sql_generation_prompt import (
    SQL_GENERATION_PROMPT,
)

from app.services.openrouter_service import (
    OpenRouterService,
)

from app.services.schema_service import (
    SchemaService,
)


class SQLService:

    @staticmethod
    def generate_sql(question: str) -> str:

        schema = (
            SchemaService.get_database_schema()
        )

        prompt = SQL_GENERATION_PROMPT.format(
            schema=schema,
            question=question,
        )

        sql = OpenRouterService.generate_text(
            prompt
        )

        return sql.strip()
