from src.metrics.structural_fidelity import StructuralFidelityMetrics

def test_structural_fidelity_metrics():
    metrics = StructuralFidelityMetrics()
    result = metrics.compute({}, {})
    assert "component_fidelity" in result
