# Modelica2SysMLv2 Pipeline: Etapas y Detalles

## 1. Extracción
- **Archivo:** `src/extractors/modelica_extractor.py`
- **Descripción:** Extrae componentes, conexiones, parámetros y jerarquía de modelos Modelica usando OpenModelica/OMPython.
- **Extensible:** Puedes añadir extractores específicos en `src/extractors/`.

## 2. Serialización
- **Archivo:** `src/serializers/json_serializer.py`
- **Descripción:** Serializa el IR extraído a JSON validado con Pydantic.
- **Soporte YAML:** Ver `src/serializers/yaml_serializer.py`.

## 3. Mapeo Semántico
- **Archivo:** `src/mappers/semantic_mapper.py`, `src/mappers/rule_based_mapper.py`
- **Descripción:** Mapea el IR a SysML v2 usando reglas y/o agentes LLM.
- **Prompts:** Estructurados en `src/prompts/`.

## 4. Generación LLM
- **Archivo:** `src/agents/llm_agent.py`
- **Descripción:** Genera código SysML v2 a partir del IR mapeado.
- **Agentes:** Generador, validador, reparador (`src/agents/`).

## 5. Validación
- **Archivos:** `src/validators/structural_validator.py`, `src/validators/ast_validator.py`, `src/validators/semantic_validator.py`
- **Descripción:** Valida sintaxis, alineación AST y semántica. Calcula métricas de fidelidad.

## 6. Reparación
- **Archivo:** `src/agents/repair_agent.py`
- **Descripción:** Corrige automáticamente el código SysML v2 si falla la validación.

## 7. Métricas y Logging
- **Archivos:** `src/metrics/`, `src/utils/logging.py`, `src/utils/experiment_tracker.py`
- **Descripción:** Calcula y agrega métricas, guarda logs y resultados reproducibles.

## Orquestación
- **Archivo:** `src/orchestrator/pipeline.py`
- **Descripción:** Ejecuta todo el pipeline de manera reproducible y modular.

---

Consulta el README y los notebooks para ejemplos de uso y reproducibilidad.
