MODEL_COST = {
    "accounts/fireworks/models/llama-v3p1-8b-instruct": 1,
    "accounts/fireworks/models/qwen3-30b-a3b-instruct-2507": 3,
    "accounts/fireworks/models/deepseek-v3": 5,
}


def estimate_cost(model: str, tokens: int):

    multiplier = MODEL_COST.get(model, 1)

    return multiplier * tokens