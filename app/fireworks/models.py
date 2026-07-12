# ALLOWED_MODELS = [
#     "accounts/fireworks/models/llama-v3p1-8b-instruct",
#     "accounts/fireworks/models/qwen3-30b-a3b-instruct-2507",
#     "accounts/fireworks/models/deepseek-v3",
# ]

from dataclasses import dataclass

@dataclass
class ModelInfo:
    name: str
    display_name: str
    cost_rank: int
    max_tokens: int


# ======================================================
# Allowed Fireworks Models
# Replace these model IDs with the exact IDs provided
# for your hackathon account if they differ.
# ======================================================

LLAMA_8B = ModelInfo(
    name="accounts/fireworks/models/llama-v3p1-8b-instruct",
    display_name="Llama 3.1 8B Instruct",
    cost_rank=1,
    max_tokens=8192,
)

QWEN_30B = ModelInfo(
    name="accounts/fireworks/models/qwen3-30b-a3b-instruct-2507",
    display_name="Qwen3 30B A3B Instruct",
    cost_rank=2,
    max_tokens=32768,
)

DEEPSEEK_V3 = ModelInfo(
    name="accounts/fireworks/models/deepseek-v3",
    display_name="DeepSeek V3",
    cost_rank=3,
    max_tokens=32768,
)


# Ordered from cheapest → most capable
ALLOWED_MODELS = [
    LLAMA_8B,
    QWEN_30B,
    DEEPSEEK_V3,
]