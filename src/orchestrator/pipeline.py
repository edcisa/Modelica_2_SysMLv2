"""
Pipeline Orchestrator
"""
from typing import Any

class PipelineOrchestrator:
    def __init__(self, config: Any):
        self.config = config

    def run(self):
        """
        Executes the full Modelica2SysMLv2 pipeline step by step:
        1. Extraction
        2. Serialization
        3. Mapping (LLM or rule-based)
        4. Generation (LLM agent)
        5. Validation (structural, AST, semantic)
        6. Repair (if needed)
        7. Metrics computation
        8. Logging and output
        """
        from src.extractors.modelica_extractor import OpenModelicaExtractor
        from src.serializers.json_serializer import JSONSerializer, ModelicaIR
        from src.mappers.semantic_mapper import SemanticMapper
        from src.agents.llm_agent import MockLLMAgent
        from src.agents.validator_agent import ValidatorAgent
        from src.agents.repair_agent import RepairAgent
        from src.validators.structural_validator import StructuralValidator
        from src.validators.ast_validator import ASTValidator
        from src.validators.semantic_validator import SemanticValidator
        from src.parsers.sysml_parser import SysMLv2Parser
        from src.metrics.structural_fidelity import StructuralFidelityMetrics
        from src.metrics.precision_metrics import PrecisionMetrics
        from src.utils.logging import setup_logging
        from src.utils.determinism import set_seed
        import os
        import json

        setup_logging()
        config = self.config
        set_seed(config.get("seed", 42))

        # 1. Extraction
        extractor = OpenModelicaExtractor()
        model_path = config["extractor"]["model_path"]
        ir_dict = extractor.extract(model_path)

        # 2. Serialization
        ir = ModelicaIR(**ir_dict)
        json_data = JSONSerializer.serialize(ir)

        # 3. Mapping (LLM or rule-based)
        mapper = SemanticMapper()
        sysml_code = mapper.map(ir_dict)

        # 4. Generation (LLM agent)
        agent = MockLLMAgent()
        sysml_code = agent.generate(sysml_code)

        # 5. Validation (structural, AST, semantic)
        validator = StructuralValidator()
        is_valid = validator.validate(sysml_code, ir_dict)
        ast_validator = ASTValidator()
        sysml_parser = SysMLv2Parser()
        sysml_ast = sysml_parser.parse(sysml_code)
        ast_valid = ast_validator.validate(ir_dict, sysml_ast)
        semantic_validator = SemanticValidator()
        semantic_valid = semantic_validator.validate(ir_dict, sysml_code)

        # 6. Repair (if needed)
        if not (is_valid and ast_valid and semantic_valid):
            repair_agent = RepairAgent()
            sysml_code = repair_agent.generate("Repair prompt")
            # Re-validate after repair
            is_valid = validator.validate(sysml_code, ir_dict)
            sysml_ast = sysml_parser.parse(sysml_code)
            ast_valid = ast_validator.validate(ir_dict, sysml_ast)
            semantic_valid = semantic_validator.validate(ir_dict, sysml_code)

        # 7. Metrics computation
        metrics = StructuralFidelityMetrics()
        results = metrics.compute(sysml_ast, ir_dict)
        precision_metrics = PrecisionMetrics()
        precision = precision_metrics.compute(sysml_ast, ir_dict)

        # 8. Logging and output
        output_dir = config.get("output_dir", "reports/tmp/")
        os.makedirs(output_dir, exist_ok=True)
        with open(os.path.join(output_dir, "extracted.json"), "w") as f:
            f.write(json_data)
        with open(os.path.join(output_dir, "generated.sysml"), "w") as f:
            f.write(sysml_code)
        with open(os.path.join(output_dir, "metrics.json"), "w") as f:
            json.dump(results, f, indent=2)
        with open(os.path.join(output_dir, "precision.json"), "w") as f:
            json.dump(precision, f, indent=2)
        print("Pipeline completed. Outputs written to:", output_dir)
