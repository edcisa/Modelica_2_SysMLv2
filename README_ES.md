# Modelica2SysMLv2: Pipeline de Transformación Semántica Asistida por IA

Este repositorio contiene el código, datos, experimentos y documentación para la transformación reproducible de modelos Modelica a SysML v2, siguiendo los estándares de ingeniería de software y reproducibilidad para artefactos de investigación de alto impacto.

## Estructura del Repositorio

- `src/` — Código fuente modular (extractores, serializadores, mapeadores, agentes, validadores, métricas, orquestador, utilidades, prompts, esquemas, configuración)
- `datasets/` — Benchmarks y datasets de entrada/salida
- `reports/` — Resultados, métricas, logs y manifiestos de experimentos
- `notebooks/` — Ejemplos reproducibles y análisis
- `scripts/` — Entrypoints CLI para pipeline, benchmarks y métricas
- `tests/` — Pruebas unitarias y de integración
- `docs/` — Diagramas y documentación extendida

## Pipeline Completo

1. **Extracción**: Obtención de estructura Modelica con OpenModelica/OMPython
2. **Serialización**: IR JSON validado con Pydantic
3. **Mapeo Semántico**: Reglas y agentes LLM
4. **Generación LLM**: Código SysML v2
5. **Validación**: Sintaxis, AST, semántica, métricas
6. **Reparación**: Corrección automática si falla validación
7. **Métricas y Logging**: Resultados reproducibles y trazables

## Ejecución Rápida

```bash
poetry install
poetry run python scripts/run_pipeline.py --config src/config/example.yaml
```

## Reproducibilidad

- Dockerfile y manifiestos reproducibles
- Semillas deterministas y variables de entorno
- CI/CD con GitHub Actions

## Contacto y Citas

Para dudas, sugerencias o citas académicas, consulta el README principal y el archivo CITATION.cff.
