# Modelica2SysMLv2: AI-Assisted Semantic Transformation Pipeline


[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/release/python-3120/)

---

## Architecture Diagram

See architecture documentation: [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)

---


## Pipeline Overview

Modelica2SysMLv2 es un framework modular, reproducible y de calidad investigadora para la transformación semántica asistida por IA de modelos Modelica a representaciones arquitectónicas SysML v2. El pipeline aprovecha OpenModelica, agentes LLM y validación rigurosa para asegurar traducción de alta fidelidad.

---

## Pipeline Stages

1. **Extraction**: Los modelos Modelica se extraen usando adaptadores OpenModelica/OMPython, obteniendo componentes, conectores, parámetros y jerarquía.
2. **Serialization**: La estructura extraída se serializa a un IR JSON validado con Pydantic.
3. **Semantic Mapping**: El IR se mapea a elementos SysML v2 usando mapeadores por reglas y LLM. Los prompts están estructurados para reproducibilidad.
4. **LLM Generation**: Agentes LLM generan código SysML v2 a partir del IR mapeado, usando prompts de sistema y corrección.
5. **Validation**: El código SysML v2 generado se valida en sintaxis, alineación AST y consistencia semántica. Se computan métricas de fidelidad estructural.
6. **Repair**: Si la validación falla, un agente de reparación intenta corregir el código y se repite el ciclo de validación.
7. **Metrics & Logging**: Todos los resultados, métricas y logs de experimentos se guardan para reproducibilidad y benchmarking.

---

## Features
- **Extracción Modelica**: Extractores OpenModelica/OMPython para componentes, conectores, parámetros y jerarquía.
- **IR JSON**: Representaciones intermedias tipadas y validadas con Pydantic.
- **Mapeo Semántico**: Mapeo por reglas y LLM a SysML v2.
- **Agentes LLM**: Generador, validador y reparador modulares con prompts estructurados.
- **Validación**: Validación sintáctica, AST y semántica con métricas de fidelidad estructural.
- **Benchmarking**: 20+ casos benchmark, agregación de métricas y tracking de experimentos.
- **Reproducibilidad**: Configs deterministas, Docker, CI/CD y empaquetado de artefactos de investigación.

---

## Installation

```bash
# Clone repository
$ git clone https://github.com/your-org/Modelica2Sysmlv2.git
$ cd Modelica2Sysmlv2

# Install Poetry
$ pip install poetry

# Install dependencies
$ poetry install
```

---

## Quickstart

```bash
# Run extraction and transformation pipeline
$ poetry run modelica2sysmlv2 run --config src/config/example.yaml
```

---

## Reproducibility Guide

- All experiments are fully reproducible via provided configs and Docker.
- Deterministic seeds and environment variables ensure consistent results.
- See [REPRODUCIBILITY.md](docs/REPRODUCIBILITY.md) for details.

---

## Benchmark Instructions

- Place Modelica models in `datasets/benchmarks/`.
- Run the benchmark pipeline:

```bash
$ poetry run modelica2sysmlv2 benchmark --manifest src/config/benchmark_manifest.yaml
```

- Results and metrics are saved in `reports/`.

---

## Dataset Structure

```
datasets/
  benchmarks/
    case01/
      model.mo
      extracted.json
      generated.sysml
      metrics.csv
    ...
```

---

## Configuration Example

See `src/config/example.yaml` for a full configuration template.

---

## Experiment Execution

- Launch experiments with:

```bash
$ poetry run modelica2sysmlv2 experiment --manifest reports/experiment_manifest.yaml
```

---

## Evaluation Methodology

- Structural fidelity, component/connection/parameter metrics
- AST alignment and semantic checks
- Aggregated CSV and visual reports

---

## Limitations

- LLM-based mapping may require API keys (see `.env.example`).
- Some integrations are stubbed/mocked for reproducibility.

---

## Citation

If you use this framework, please cite:

```bibtex
@article{your2026modelica2sysmlv2,
  title={AI-Assisted Semantic Transformation from Modelica to SysML v2},
  author={Your, Name and Collaborator, Name},
  journal={Journal of Systems and Software},
  year={2026}
}
```

---

## Research Context

This repository is a research artifact accompanying the paper:

> "AI-Assisted Semantic Transformation from Modelica to SysML v2: A Validation-Driven Pipeline for MBSE Interoperability"

---

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE).
