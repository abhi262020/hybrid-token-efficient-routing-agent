from enum import Enum


class TaskType(str, Enum):
    GENERAL = "general"
    MATH = "math"
    CODING = "coding"
    TRANSLATION = "translation"
    SUMMARIZATION = "summarization"
    REASONING = "reasoning"
    SQL = "sql"
    GRAMMAR = "grammar"