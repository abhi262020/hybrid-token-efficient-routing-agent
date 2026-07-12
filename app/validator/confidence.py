def calculate_confidence(response: str) -> float:
    """
    Simple confidence estimator.
    Replace with a better model later.
    """

    length = len(response.strip())

    if length > 300:
        return 0.98

    if length > 150:
        return 0.90

    if length > 50:
        return 0.80

    return 0.50