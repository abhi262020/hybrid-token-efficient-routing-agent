from dataclasses import dataclass


@dataclass
class ModelInfo:
    name: str
    cost_level: int
    max_complexity: int


MODELS = [
    ModelInfo(
        name="accounts/fireworks/models/gpt-oss-120b",
        cost_level=1,
        max_complexity=10,
    ),
]