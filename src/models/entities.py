from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional

@dataclass
class Contract:
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
    clause_text: str
    risk_level: str
    contract_id: Optional[int] = None
    clause_id: Optional[int] = None
