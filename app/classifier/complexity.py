from app.classifier.task_types import TaskType


def estimate(prompt: str, task: TaskType) -> int:

    score = 1

    score += len(prompt.split()) // 15

    if task == TaskType.CODING:
        score += 3

    elif task == TaskType.REASONING:
        score += 5

    elif task == TaskType.SQL:
        score += 2

    return min(score, 10)