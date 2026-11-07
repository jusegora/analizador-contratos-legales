from src.database.db_manager import DatabaseManager
from src.models.entities import Contract, Clause

class ContractRepository:
    def __init__(self, db_manager: DatabaseManager):
        self.db = db_manager

    def save_contract_with_clauses(self, contract: Contract) -> int:
        """Guarda el contrato y sus cláusulas asociadas en una transacción."""
        if not self.db.connection:
            self.db.connect()
            
        try:
            with self.db.connection.cursor() as cursor:
                # 1. Insertar Contrato
                cursor.execute(
                    "INSERT INTO contracts (file_name, status) VALUES (%s, %s) RETURNING contract_id;",
                    (contract.file_name, 'PROCESSED')
                )
                contract_id = cursor.fetchone()[0]
                contract.contract_id = contract_id
                
                # 2. Insertar Cláusulas
                for clause in contract.clauses:
                    cursor.execute(
                        "INSERT INTO clauses (contract_id, clause_text, risk_level) VALUES (%s, %s, %s);",
                        (contract_id, clause.clause_text, clause.risk_level)
                    )
            print(f"✅ Contrato '{contract.file_name}' y {len(contract.clauses)} cláusulas guardadas en la nube.")
            return contract_id
        except Exception as e:
            print(f"❌ Error al guardar en BD: {e}")
            raise
