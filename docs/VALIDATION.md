# Validación y Métricas

## Validadores
- `src/validators/structural_validator.py`: Valida la estructura del SysML v2 generado contra el IR de Modelica.
- `src/validators/ast_validator.py`: Valida la alineación de AST entre Modelica y SysML v2.
- `src/validators/semantic_validator.py`: Chequea la preservación semántica.

## Métricas
- `src/metrics/structural_fidelity.py`: Fidelidad estructural (componentes, conexiones, parámetros).
- `src/metrics/precision_metrics.py`: Precisión y recall de la transformación.
- `src/metrics/aggregation.py`: Agregación de métricas en benchmarks.

## Ejecución de Validación

```python
from src.validators.structural_validator import StructuralValidator
validator = StructuralValidator()
assert validator.validate(sysml_code, ir_dict)
```

## Ejecución de Métricas

```python
from src.metrics.structural_fidelity import StructuralFidelityMetrics
metrics = StructuralFidelityMetrics()
results = metrics.compute(sysml_ast, ir_dict)
```
