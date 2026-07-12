from loguru import logger


logger.add(
    "logs/router.log",
    rotation="10 MB"
)


def log_route(model, tokens, confidence):

    logger.info(
        f"Model={model} "
        f"Tokens={tokens} "
        f"Confidence={confidence}"
    )