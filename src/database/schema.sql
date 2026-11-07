-- ==========================================
-- LEGALTECH CONTRACT ANALYZER - POSTGRESQL SCHEMA
-- Author: jusegora
-- ==========================================

-- Limpieza previa (Idempotencia para entornos de producción)
DROP TABLE IF EXISTS clauses CASCADE;
DROP TABLE IF EXISTS contracts CASCADE;
DROP TABLE IF EXISTS audit_log CASCADE;
DROP FUNCTION IF EXISTS audit_clauses_insert() CASCADE;

-- 1. TABLA DE CONTRATOS
CREATE TABLE contracts (
    contract_id SERIAL PRIMARY KEY,
    file_name VARCHAR(255) NOT NULL,
    upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(50) DEFAULT 'PENDING' CHECK (status IN ('PENDING', 'PROCESSED', 'ERROR'))
);

-- 2. TABLA DE CLÁUSULAS
CREATE TABLE clauses (
    clause_id SERIAL PRIMARY KEY,
    contract_id INTEGER NOT NULL REFERENCES contracts(contract_id) ON DELETE CASCADE,
    clause_text TEXT NOT NULL,
    risk_level VARCHAR(20) CHECK (risk_level IN ('LOW', 'MEDIUM', 'HIGH', 'CRITICAL')),
    extracted_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 3. ÍNDICES
CREATE INDEX idx_contract_status ON contracts(status);
CREATE INDEX idx_clause_risk ON clauses(risk_level);

-- 4. TABLA DE AUDITORÍA
CREATE TABLE audit_log (
    log_id SERIAL PRIMARY KEY,
    table_name VARCHAR(50),
    action_type VARCHAR(20),
    action_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    performed_by VARCHAR(50) DEFAULT CURRENT_USER
);

-- 5. TRIGGER DE AUDITORÍA
CREATE OR REPLACE FUNCTION audit_clauses_insert()
RETURNS TRIGGER AS $func$
BEGIN
    INSERT INTO audit_log (table_name, action_type)
    VALUES ('CLAUSES', 'INSERT');
    RETURN NEW;
END;
$func$ LANGUAGE plpgsql;

CREATE TRIGGER trg_audit_clauses
AFTER INSERT ON clauses
FOR EACH ROW
EXECUTE FUNCTION audit_clauses_insert();
