import os
from src.database.db_manager import DatabaseManager

if __name__ == "__main__":
    print("🚀 Iniciando configuración de la base de datos LegalTech...")
    
    # Ruta al archivo SQL que creamos anteriormente
    schema_file = os.path.join("src", "database", "schema.sql")
    
    db = DatabaseManager()
    
    try:
        db.connect()
        db.execute_schema(schema_file)
    except Exception as e:
        print(f"❌ Fallo en el proceso de configuración: {e}")
    finally:
        db.close()
