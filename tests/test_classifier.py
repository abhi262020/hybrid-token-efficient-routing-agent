from app.classifier.intent_classifier import classify


def test_general_question():

    task = classify(
        "What is the capital of India?"
    )

    assert task is not None


def test_code_prompt():

    task = classify(
        "Write a Python sorting algorithm."
    )

    assert task is not None