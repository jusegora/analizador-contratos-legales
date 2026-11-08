import re
import spacy

class ClauseAnalyzer:
    def __init__(self):
        self.nlp = spacy.blank("es")
        self.reglas = {
            "CRITICAL": [r"penalizaci[oó]n", r"cl[aá]usula penal", r"indemnizaci[oó]n"],
            "HIGH": [r"confidencialidad", r"no competencia", r"exclusividad"],
            "MEDIUM": [r"terminaci[oó]n", r"rescisi[oó]n", r"renovaci[oó]n autom[aá]tica"]
        }

    def analizar(self, texto):
        resultados = []
        # Separar por parrafos o puntos
        bloques = re.split(r'\n\n|\.\s', texto)
        
        for b in bloques:
            if not b.strip():
                continue
            
            b_lower = b.lower()
            for nivel, palabras in self.reglas.items():
                for p in palabras:
                    if re.search(p, b_lower):
                        resultados.append({"texto": b.strip(), "riesgo": nivel})
                        break
        return resultados
