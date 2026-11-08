import os
from src.database.db_manager import DatabaseManager
from src.database.repository import ContractRepository
from src.extractors.clause_analyzer import ClauseAnalyzer
from src.models.entities import Contract, Clause

def run_pipeline():
    print("Iniciando procesamiento de contratos...")
    
    db = DatabaseManager()
    repo = ContractRepository(db)
    analyzer = ClauseAnalyzer()
    
    file_path = os.path.join("data", "raw", "contrato_prueba.txt")
    file_name = "contrato_prueba.txt"
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            text_content = f.read()
            
        print("Analizando texto...")
        extracted_data = analyzer.analyze_text(text_content)
        
        contract = Contract(file_name=file_name)
        
        for item in extracted_data:
            clause = Clause(clause_text=item["clause_text"], risk_level=item["risk_level"])
            contract.clauses.append(clause)
            
        print(f"Clausulas detectadas: {len(contract.clauses)}")
        
        if contract.clauses:
            repo.save_contract_with_clauses(contract)
        else:
            print("No se encontraron clausulas de riesgo.")
            
        print("\nVerificando datos en la nube:")
        with db.connection.cursor() as cursor:
            cursor.execute("""
                SELECT c.file_name, cl.risk_level, COUNT(cl.clause_id) 
                FROM contracts c
                JOIN clauses cl ON c.contract_id = cl.contract_id
                GROUP BY c.file_name, cl.risk_level;
            """)
            results = cursor.fetchall()
            for row in results:
                print(f"   Archivo: {row[0]} | Riesgo: {row[1]} | Cantidad: {row[2]}")
                
    except Exception as e:
        print(f"Error: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    run_pipeline()
