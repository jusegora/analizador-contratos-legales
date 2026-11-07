from pypdf import PdfReader
from typing import Optional

class PDFParser:
    """Clase encargada de leer documentos PDF y extraer su texto."""
    
    @staticmethod
    def extract_text(file_path: str) -> Optional[str]:
        try:
            reader = PdfReader(file_path)
            text = ""
            for page in reader.pages:
                extracted = page.extract_text()
                if extracted:
                    text += extracted + "\n\n"
            return text if text.strip() else None
        except Exception as e:
            print(f"❌ Error al leer el PDF: {e}")
            return None
