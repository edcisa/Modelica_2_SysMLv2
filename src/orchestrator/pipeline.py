"""Pipeline orchestration for Modelica-to-SysML transformation."""

from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Any

from loguru import logger

from src.agents.llm_agent import MockLLMAgent
from src.agents.repair_agent import RepairAgent
from src.agents.validator_agent import ValidatorAgent
from src.extractors.modelica_extractor import OpenModelicaExtractor
from src.mappers.rule_based_mapper import RuleBasedMapper
from src.mappers.semantic_mapper import SemanticMapper
from src.metrics.precision_metrics import PrecisionMetrics
from src.metrics.structural_fidelity import StructuralFidelityMetrics
from src.parsers.sysml_parser import SysMLv2Parser
from src.serializers.json_serializer import JSONSerializer, ModelicaIR
from src.utils.determinism import set_seed
from src.utils.logging import setup_logging
from src.validators.ast_validator import ASTValidator
from src.validators.semantic_validator import SemanticValidator
from src.validators.structural_validator import StructuralValidator

class PipelineOrchestrator:
    def __init__(self, config: Any):
        self.config = config

    def run(self) -> dict[str, Any]:
        """Execute the full transformation workflow and return a run summary."""
        setup_logging(self.config.get("log_level", "INFO"))
        set_seed(int(self.config.get("seed", 42)))

        extractor = OpenModelicaExtractor()
        mapping_type = str(self.config.get("mapper", {}).get("type", "semantic"))
        mapper = SemanticMapper() if mapping_type == "semantic" else RuleBasedMapper()

        generator_agent = MockLLMAgent()
        validator_agent = ValidatorAgent()
        repair_agent = RepairAgent()

        structural_validator = StructuralValidator()
        ast_validator = ASTValidator()
        semantic_validator = SemanticValidator()
        sysml_parser = SysMLv2Parser()

        model_path = self.config.get("extractor", {}).get("model_path", "")
        output_dir = Path(self.config.get("output_dir", "reports/tmp"))
        output_dir.mkdir(parents=True, exist_ok=True)

        logger.info("Stage 1/8: extraction")
        ir_dict = extractor.extract(model_path)

        logger.info("Stage 2/8: serialization")
        ir = ModelicaIR(**ir_dict)
        ir_json = JSONSerializer.serialize(ir)

        logger.info("Stage 3/8: semantic mapping")
        mapped_prompt = mapper.map(ir_dict)

        logger.info("Stage 4/8: LLM generation")
        sysml_code = generator_agent.generate(mapped_prompt, {"candidate": mapped_prompt})

        logger.info("Stage 5-6/8: validation and repair loop")
        max_repair_iterations = int(self.config.get("max_repair_iterations", 2))
        checks = {"structural": False, "ast": False, "semantic": False}
        repair_attempts = 0

        while True:
            sysml_ast = sysml_parser.parse(sysml_code)
            checks = {
                "structural": structural_validator.validate(sysml_code, ir_dict),
                "ast": ast_validator.validate(ir_dict, sysml_ast),
                "semantic": semantic_validator.validate(ir_dict, sysml_code),
            }
            if all(checks.values()) or repair_attempts >= max_repair_iterations:
                break

            repair_attempts += 1
            sysml_code = repair_agent.generate(
                "repair invalid sysml",
                {
                    "candidate": sysml_code,
                    "model_name": ir_dict.get("model_name", "RecoveredModel"),
                    "checks": checks,
                },
            )

        validation_summary = validator_agent.generate("validate", {"checks": checks})

        logger.info("Stage 7/8: metrics")
        fidelity_metrics = StructuralFidelityMetrics().compute(sysml_ast, ir_dict)
        precision_metrics = PrecisionMetrics().compute(sysml_ast, ir_dict)
        combined_metrics = {**fidelity_metrics, **precision_metrics}

        logger.info("Stage 8/8: persist artifacts")
        (output_dir / "extracted.json").write_text(ir_json, encoding="utf-8")
        (output_dir / "generated.sysml").write_text(sysml_code, encoding="utf-8")
        (output_dir / "validation.txt").write_text(validation_summary, encoding="utf-8")
        JSONSerializer.save_dict(combined_metrics, str(output_dir / "metrics.json"))

        with open(output_dir / "metrics.csv", "w", newline="", encoding="utf-8") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=list(combined_metrics.keys()))
            writer.writeheader()
            writer.writerow(combined_metrics)

        run_summary = {
            "model_name": ir_dict.get("model_name", "UnknownModel"),
            "model_path": model_path,
            "output_dir": str(output_dir),
            "checks": checks,
            "repair_attempts": repair_attempts,
            "metrics": combined_metrics,
            "status": "ok" if all(checks.values()) else "degraded",
        }

        with open(output_dir / "run_summary.json", "w", encoding="utf-8") as summary_file:
            json.dump(run_summary, summary_file, indent=2)

        return run_summary
