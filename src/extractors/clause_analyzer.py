import re
import spacy
from typing import List, Dict

class ClauseAnalyzer:
    """
    Motor NLP basado en reglas para identificar cláusulas de riesgo en contratos.
    Utiliza spaCy (tokenizador ligero) y Expresiones Regulares.
    """
    def __init__(self) -> None:
        # Usamos un pipeline en blanco para no consumir RAM (ideal para 4GB)
        self.nlp = spacy.blank("es")
        
        # Diccionario de reglas de negocio (Legal Tech)
        # En un entorno real, esto vendría de una base de datos o configuración.
        self.risk_rules: Dict[str, Dict] = {
            "CRITICAL": {
                "keywords": [r"penalizaci[oó]n", r"cl[aá]usula penal", r"indemnizaci[oó]n"],
                "description": "Cláusulas que implican sanciones económicas altas."
            },
            "HIGH": {
                "keywords": [r"confidencialidad", r"no competencia", r"exclusividad"],
                "description": "Restricciones operativas o de secreto."
            },
            "MEDIUM": {
                "keywords": [r"terminaci[oó]n", r"rescisi[oó]n", r"renovaci[oó]n autom[aá]tica"],
                "description": "Condiciones de salida o duración del contrato."
            }
        }

    def analyze_text(self, text: str) -> List[Dict[str, str]]:
        """Analiza el texto y devuelve una lista de cláusulas detectadas."""
        extracted_clauses = []
        
        # Dividimos por párrafos o puntos seguidos para analizar bloque por bloque
        paragraphs = re.split(r'\n\n|\.\s', text)
        
        for paragraph in paragraphs:
            if not paragraph.strip():
                continue
                
            paragraph_lower = paragraph.lower()
            
            for risk_level, rule in self.risk_rules.items():
                for keyword in rule["keywords"]:
                    if re.search(keyword, paragraph_lower):
                        extracted_clauses.append({
                            "clause_text": paragraph.strip(),
                            "risk_level": risk_level
                        })
                        break # Si ya detectó riesgo en este párrafo, no revisar otras palabras del mismo nivel
                        
        return extracted_clauses
