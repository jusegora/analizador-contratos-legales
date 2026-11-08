# Analizador de Contratos LegalTech

Este es un proyecto personal que desarrollé para automatizar la lectura de contratos y detectar cláusulas de riesgo.

## Descripcion
El script lee archivos de texto, usa reglas de expresiones regulares para encontrar palabras clave (como "penalización" o "confidencialidad") y guarda los resultados en una base de datos PostgreSQL en Neon.tech.

## Como funciona
- `src/database/db_manager.py`: Maneja la conexion a la base de datos.
- `src/extractors/clause_analyzer.py`: Contiene la logica para buscar las palabras clave.
- `src/models/entities.py`: Define las clases de Contrato y Clausula.
- `main.py`: Ejecuta el flujo completo.

## Tecnologias
- Python 3
- PostgreSQL (Neon.tech)
- SpaCy (para tokenizacion basica)

## Uso
1. Configurar el archivo `.env` con la URL de la base de datos.
2. Ejecutar `python main.py`.
