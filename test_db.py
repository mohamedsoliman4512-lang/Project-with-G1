from sqlalchemy import text

from app.database.connection import DatabaseConnection

session = DatabaseConnection.get_session()

result = session.execute(
    text("SELECT COUNT(*) FROM products")
)

print("Products:", result.scalar())
