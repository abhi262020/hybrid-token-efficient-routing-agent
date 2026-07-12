from app.classifier.task_types import TaskType


def classify(prompt: str) -> TaskType:

    text = prompt.lower()

    if "python" in text or "java" in text or "code" in text:
        return TaskType.CODING

    if "translate" in text:
        return TaskType.TRANSLATION

    if "sql" in text:
        return TaskType.SQL

    if "grammar" in text:
        return TaskType.GRAMMAR

    if "sum" in text or "calculate" in text:
        return TaskType.MATH

    return TaskType.GENERAL