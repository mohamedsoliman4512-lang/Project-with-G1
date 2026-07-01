from sqlalchemy import text

from app.database.connection import DatabaseConnection


class DatabaseTool:
    """Tool for executing SQL queries."""

    @staticmethod
    def execute_query(query: str):
        session = DatabaseConnection.get_session()

        try:
            result = session.execute(text(query))

            rows = []

            for row in result:

                row_dict = {}

                for key, value in row._mapping.items():

                    if isinstance(value, memoryview):
                        row_dict[key] = "<binary_data>"
                    else:
                        row_dict[key] = value

                rows.append(row_dict)

            return rows

        finally:
            session.close()
