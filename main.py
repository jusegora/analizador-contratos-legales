import os
from src.database.db_manager import DatabaseManager
from src.database.repository import ContractRepository
from src.extractors.clause_analyzer import ClauseAnalyzer
from src.models.entities import Contract, Clause

def run():
    db = DatabaseManager()
    repo = ContractRepository(db)
    analyzer = ClauseAnalyzer()
    
    ruta = os.path.join("data", "raw", "contrato_prueba.txt")
    
    try:
        with open(ruta, 'r', encoding='utf-8') as f:
            texto = f.read()
            
        hallazgos = analyzer.analizar(texto)
        contrato = Contract(file_name="contrato_prueba.txt")
        
        for h in hallazgos:
            contrato.clauses.append(Clause(clause_text=h["texto"], risk_level=h["riesgo"]))
            
        if contrato.clauses:
            repo.guardar(contrato)
            print(f"Guardadas {len(contrato.clauses)} clausulas.")
        else:
            print("Sin hallazgos.")
            
    except Exception as e:
        print(f"Fallo: {e}")
    finally:
        db.cerrar()

if __name__ == "__main__":
    run()
