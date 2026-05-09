from src.validators.structural_validator import StructuralValidator

def test_structural_validator():
    validator = StructuralValidator()
    assert validator.validate("sysml_code", {})
