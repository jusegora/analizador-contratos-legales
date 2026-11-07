import pytest
from src.extractors.clause_analyzer import ClauseAnalyzer

def test_detecta_riesgo_critico():
    analizador = ClauseAnalyzer()
    texto = "En caso de incumplimiento, se aplicará una cláusula penal del 30%."
    resultados = analizador.analyze_text(texto)
    
    assert len(resultados) == 1
    assert resultados[0]["risk_level"] == "CRITICAL"
    assert "cláusula penal" in resultados[0]["clause_text"].lower()

def test_detecta_riesgo_alto():
    analizador = ClauseAnalyzer()
    texto = "El contratista se obliga a mantener absoluta confidencialidad."
    resultados = analizador.analyze_text(texto)
    
    assert len(resultados) == 1
    assert resultados[0]["risk_level"] == "HIGH"

def test_ignora_texto_seguro():
    analizador = ClauseAnalyzer()
    texto = "El objeto del contrato es la prestación de servicios de consultoría."
    resultados = analizador.analyze_text(texto)
    
    assert len(resultados) == 0
