import os
import psycopg2
import sqlparse
from dotenv import load_dotenv

load_dotenv()

class GestorBaseDatos:
    def __init__(self):
        self.url_db = os.getenv("DATABASE_URL")
        if not self.url_db:
            raise ValueError("Falta la URL de la base de datos en el .env")
        self.conexion = None

    def conectar(self):
        try:
            self.conexion = psycopg2.connect(self.url_db)
            self.conexion.autocommit = True
            print("Conexion exitosa.")
        except Exception as e:
            print(f"Error al conectar: {e}")
            raise

    def ejecutar_script(self, ruta_sql):
        if not self.conexion:
            self.conectar()
        try:
            with open(ruta_sql, 'r', encoding='utf-8-sig') as f:
                script = f.read()
            
            sentencias = sqlparse.split(script)
            with self.conexion.cursor() as cur:
                for s in sentencias:
                    if s.strip():
                        cur.execute(s)
            print("Tablas creadas correctamente.")
        except Exception as e:
            print(f"Error en el script SQL: {e}")
            raise

    def cerrar(self):
        if self.conexion:
            self.conexion.close()
            print("Conexion cerrada.")
