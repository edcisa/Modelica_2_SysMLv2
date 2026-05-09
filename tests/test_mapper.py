from src.mappers.semantic_mapper import SemanticMapper

def test_semantic_mapper():
    mapper = SemanticMapper()
    sysml_code = mapper.map({"components": [], "connections": [], "parameters": []})
    assert isinstance(sysml_code, str)
