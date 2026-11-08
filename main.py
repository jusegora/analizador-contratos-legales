import os
from src.database.db_manager import GestorBaseDatos
from src.database.repository import ContractRepository
from src.extractors.clause_analyzer import ClauseAnalyzer
from src.models.entities import Contract, Clause

def ejecutar():
    gestor = GestorBaseDatos()
    repo = ContractRepository(gestor)
    analizador = ClauseAnalyzer()
    
    ruta = os.path.join("data", "raw", "contrato_prueba.txt")
    
    try:
        with open(ruta, 'r', encoding='utf-8') as f:
            texto = f.read()
            
        hallazgos = analizador.analizar(texto)
        contrato = Contract(file_name="contrato_prueba.txt")
        
        for h in hallazgos:
            contrato.clauses.append(Clause(clause_text=h["texto"], risk_level=h["riesgo"]))
            
        if contrato.clauses:
            repo.guardar(contrato)
            print(f"Se guardaron {len(contrato.clauses)} clausulas.")
        else:
            print("No se encontraron clausulas de riesgo.")
            
    except Exception as e:
        print(f"Error en el proceso: {e}")
    finally:
        gestor.cerrar()

if __name__ == "__main__":
    ejecutar()
