import re
import spacy

class ClauseAnalyzer:
    def __init__(self):
        self.nlp = spacy.blank("es")
        self.risk_rules = {
            "CRITICAL": {
                "keywords": [r"penalizaci[oó]n", r"cl[aá]usula penal", r"indemnizaci[oó]n"],
            },
            "HIGH": {
                "keywords": [r"confidencialidad", r"no competencia", r"exclusividad"],
            },
            "MEDIUM": {
                "keywords": [r"terminaci[oó]n", r"rescisi[oó]n", r"renovaci[oó]n autom[aá]tica"],
            }
        }

    def analyze_text(self, text):
        extracted_clauses = []
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
                        break
        return extracted_clauses
