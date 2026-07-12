import ast


def check_python(code: str) -> bool:
    """
    Returns True if Python code parses successfully.
    """

    try:
        ast.parse(code)
        return True
    except SyntaxError:
        return False