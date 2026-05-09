# Reviewer Guide: Modelica2SysMLv2

## Overview
Este repositorio es un artefacto de investigación reproducible, diseñado para revisión rigurosa en revistas de ingeniería de software.

## ¿Qué encontrará?
- Código modular, tipado y documentado
- Pipeline reproducible, configurable y extensible
- Benchmarks, experimentos y métricas
- Pruebas unitarias y scripts CLI
- Dockerfile y CI/CD
- Documentación detallada y ejemplos

## ¿Cómo revisar?
1. **Instalación**: Siga el README para instalar dependencias y reproducir experimentos.
2. **Pipeline**: Revise `src/orchestrator/pipeline.py` para la lógica completa y modular.
3. **Benchmarks**: Ejecute benchmarks con los scripts y revise los resultados en `reports/`.
4. **Validación**: Consulte los módulos de validación y métricas en `src/validators/` y `src/metrics/`.
5. **Extensión**: Pruebe agregar un extractor, mapeador o agente siguiendo los ejemplos en `docs/EXAMPLES.md`.
6. **Reproducibilidad**: Verifique los manifiestos, seeds y Dockerfile.

## Preguntas frecuentes
- ¿El pipeline es modular y extensible? **Sí**
- ¿Hay pruebas y ejemplos? **Sí**
- ¿Se puede ejecutar todo con un solo comando? **Sí**
- ¿La documentación cubre todas las etapas? **Sí**

Para dudas, consulte README, docs/ o contacte a los autores.
