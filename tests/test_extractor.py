import pytest
from src.extractors.modelica_extractor import OpenModelicaExtractor

def test_extractor_interface():
    extractor = OpenModelicaExtractor()
    result = extractor.extract("dummy.mo")
    assert isinstance(result, dict)
    assert "components" in result
    assert "connections" in result
    assert "parameters" in result
