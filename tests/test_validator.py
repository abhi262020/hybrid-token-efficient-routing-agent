from app.validator.confidence import calculate_confidence
from app.validator.quality import validate_quality


def test_confidence():

    score = calculate_confidence(
        "Artificial Intelligence is a branch of Computer Science."
    )

    assert score >= 0


def test_quality():

    quality = validate_quality(
        "This is a valid answer."
    )

    assert isinstance(quality, bool)