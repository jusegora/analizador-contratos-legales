import pytest
import os
from src.database.db_manager import DatabaseManager

def test_db_manager_loads_url():
    db = DatabaseManager()
    assert db.db_url is not None
    assert db.db_url.startswith("postgresql://")
