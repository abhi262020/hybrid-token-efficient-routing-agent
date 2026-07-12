from app.router.model_registry import MODELS


def next_model(current_name: str):

    for index, model in enumerate(MODELS):

        if model.name == current_name:

            if index + 1 < len(MODELS):
                return MODELS[index + 1]

            return model

    return MODELS[-1]