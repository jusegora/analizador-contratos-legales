import os
import psycopg2
import sqlparse
from dotenv import load_dotenv

load_dotenv()

class DatabaseManager:
    def __init__(self):
        self.db_url = os.getenv("DATABASE_URL")
        if not self.db_url:
            raise ValueError("Falta DATABASE_URL en el archivo .env")
        self.connection = None

    def connect(self):
        try:
            self.connection = psycopg2.connect(self.db_url)
            self.connection.autocommit = True
            print("Conectado a PostgreSQL")
        except Exception as e:
            print(f"Error de conexion: {e}")
            raise

    def execute_schema(self, schema_path):
        if not self.connection:
            self.connect()
        try:
            with open(schema_path, 'r', encoding='utf-8-sig') as file:
                sql_script = file.read()
            statements = sqlparse.split(sql_script)
            with self.connection.cursor() as cursor:
                for statement in statements:
                    if statement.strip():
                        cursor.execute(statement)
            print("Tablas creadas correctamente.")
        except Exception as e:
            print(f"Error al ejecutar SQL: {e}")
            raise

    def close(self):
        if self.connection:
            self.connection.close()
            print("Conexion cerrada.")
