import hashlib


def create_cache_key(prompt):

    return hashlib.sha256(
        prompt.encode()
    ).hexdigest()


def normalize(text):

    return " ".join(
        text.strip().split()
    )