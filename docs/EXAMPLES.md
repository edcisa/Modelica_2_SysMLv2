# Ejemplos de Uso y Extensión

## Ejemplo de Ejecución del Pipeline

```python
from src.orchestrator.pipeline import PipelineOrchestrator
import yaml

with open('src/config/example.yaml') as f:
    config = yaml.safe_load(f)
pipeline = PipelineOrchestrator(config)
pipeline.run()
```

## Ejemplo de Benchmark CLI

```bash
poetry run python scripts/benchmark_runner.py --manifest src/config/benchmark_manifest.yaml
```

## Ejemplo de Notebook

Ver `notebooks/Modelica2SysMLv2_Example.ipynb` para un flujo reproducible paso a paso.

## Extensión: Nuevo Extractor

Crea un archivo en `src/extractors/mi_extractor.py`:

```python
from typing import Dict, Any
class MiExtractor:
    def extract(self, model_path: str) -> Dict[str, Any]:
        # Tu lógica aquí
        return {}
```

Agrega tu extractor al pipeline modificando la configuración YAML.
