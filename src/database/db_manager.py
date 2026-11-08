import os
import psycopg2
import sqlparse
from dotenv import load_dotenv

load_dotenv()

class DatabaseManager:
    def __init__(self):
        self.db_url = os.getenv("DATABASE_URL")
        if not self.db_url:
            raise ValueError("Falta DATABASE_URL en el .env")
        self.conn = None

    def conectar(self):
        try:
            self.conn = psycopg2.connect(self.db_url)
            self.conn.autocommit = True
            print("Conectado a PostgreSQL.")
        except Exception as e:
            print(f"Error de conexion: {e}")
            raise

    def ejecutar_sql(self, ruta):
        if not self.conn:
            self.conectar()
        try:
            with open(ruta, 'r', encoding='utf-8-sig') as f:
                script = f.read()
            
            # Separar por ; para ejecutar uno a uno
            sentencias = sqlparse.split(script)
            with self.conn.cursor() as cur:
                for s in sentencias:
                    if s.strip():
                        cur.execute(s)
            print("Tablas creadas.")
        except Exception as e:
            print(f"Error en SQL: {e}")
            raise

    def cerrar(self):
        if self.conn:
            self.conn.close()
