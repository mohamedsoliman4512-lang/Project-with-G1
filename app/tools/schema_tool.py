from sqlalchemy import text

from app.database.connection import DatabaseConnection


class SchemaTool:

    @staticmethod
    def get_tables():

        session = DatabaseConnection.get_session()

        try:
            result = session.execute(
                text(
                    """
                    SELECT table_name
                    FROM information_schema.tables
                    WHERE table_schema = 'public'
                    ORDER BY table_name
                    """
                )
            )

            return [
                row[0]
                for row in result.fetchall()
            ]

        finally:
            session.close()

    @staticmethod
    def get_columns(table_name: str):

        session = DatabaseConnection.get_session()

        try:
            result = session.execute(
                text(
                    """
                    SELECT
                        column_name,
                        data_type
                    FROM information_schema.columns
                    WHERE table_name = :table_name
                    ORDER BY ordinal_position
                    """
                ),
                {
                    "table_name": table_name
                }
            )

            return [
                {
                    "name": row[0],
                    "type": row[1]
                }
                for row in result.fetchall()
            ]

        finally:
            session.close()
