from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional

@dataclass
class Contract:
    """Representa un contrato legal en el sistema."""
    file_name: str
    status: str = 'PENDING'
    contract_id: Optional[int] = None
    upload_date: Optional[datetime] = None
    clauses: List['Clause'] = None

    def __post_init__(self):
        if self.clauses is None:
            self.clauses = []

@dataclass
class Clause:
    """Representa una cláusula extraída con su nivel de riesgo."""
    clause_text: str
    risk_level: str # LOW, MEDIUM, HIGH, CRITICAL
    contract_id: Optional[int] = None
    clause_id: Optional[int] = None
