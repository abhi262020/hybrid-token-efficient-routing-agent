def validate_quality(response: str) -> bool:

    if not response:
        return False

    if len(response.strip()) < 20:
        return False

    banned = [
        "I don't know",
        "No idea",
        "Cannot answer"
    ]

    text = response.lower()

    for word in banned:
        if word.lower() in text:
            return False

    return True