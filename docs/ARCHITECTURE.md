# Arquitectura del Proyecto

## Capas Principales

- **Extractores**: Obtienen la estructura de modelos Modelica (componentes, conexiones, parámetros, jerarquía).
- **Serializadores**: Transforman la estructura extraída a IR JSON/YAML validado.
- **Mapeadores**: Traducen el IR a SysML v2 usando reglas y/o agentes LLM.
- **Agentes**: Generan, validan y reparan código SysML v2.
- **Validadores**: Chequean sintaxis, alineación AST y semántica.
- **Métricas**: Calculan fidelidad estructural, precisión y agregación.
- **Orquestador**: Ejecuta el pipeline completo, configurable y reproducible.
- **Utils**: Logging, determinismo, tracking de experimentos.

## Diagrama (ver docs/architecture.png)

## Extensión
- Añada nuevos extractores, mapeadores o agentes creando archivos en los módulos correspondientes y actualizando la configuración YAML.

## Ejemplo de Flujo
1. `run_pipeline.py` carga configuración YAML
2. Orquestador ejecuta cada etapa
3. Resultados y métricas se guardan en `reports/`
