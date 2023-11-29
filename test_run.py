"""
Tests
"""
from run import import_data

def test_import_data():
  data = import_data()
  assert data.shape[0] > 0
