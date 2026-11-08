# Analizador de Contratos Legales

**Por:** jusegora | Abogado & AI Solutions Architect

Herramienta desarrollada para procesar contratos de texto, detectar cláusulas de riesgo y almacenarlas en una base de datos PostgreSQL.

## Funcionamiento
El sistema lee un archivo de texto, busca palabras clave relacionadas con penalizaciones o confidencialidad usando expresiones regulares, y guarda los hallazgos en la nube. 

## Tecnologias
- Python 3.11
- PostgreSQL (Neon.tech)
- SpaCy

## Como ejecutar
1. Configurar las credenciales en el archivo `.env`.
2. Ejecutar el comando: `python main.py`
