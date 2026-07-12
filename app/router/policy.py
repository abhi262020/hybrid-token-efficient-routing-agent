from app.router.model_registry import MODELS


def choose_model(complexity: int):

    for model in MODELS:
        if complexity <= model.max_complexity:
            return model

    return MODELS[-1]