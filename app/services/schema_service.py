
from app.tools.schema_tool import SchemaTool


class SchemaService:

    @staticmethod
    def get_database_schema():

        tables = SchemaTool.get_tables()

        schema_text = ""

        for table in tables:

            schema_text += f"\nTable: {table}\n"

            columns = SchemaTool.get_columns(table)

            for column in columns:
                schema_text += (
                    f"- {column['name']} "
                    f"({column['type']})\n"
                )

        return schema_text.strip()
