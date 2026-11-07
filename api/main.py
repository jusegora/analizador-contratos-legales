from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.extractors.clause_analyzer import ClauseAnalyzer

app = FastAPI(
    title="API LegalTech",
    description="API para analizar contratos y detectar riesgos.",
    version="1.0"
)

analyzer = ClauseAnalyzer()

class ContractRequest(BaseModel):
    contract_text: str = Field(..., description="Texto del contrato", min_length=10)

class ClauseResponse(BaseModel):
    clause_text: str
    risk_level: str

class AnalysisResponse(BaseModel):
    status: str
    clauses_detected: int
    clauses: List[ClauseResponse]

@app.get("/", tags=["Salud"])
async def root():
    return {"mensaje": "API funcionando"}

@app.post("/analyze", response_model=AnalysisResponse, tags=["NLP"])
async def analyze_contract(request: ContractRequest):
    try:
        detected_clauses = analyzer.analyze_text(request.contract_text)
        return AnalysisResponse(
            status="ok",
            clauses_detected=len(detected_clauses),
            clauses=detected_clauses
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
