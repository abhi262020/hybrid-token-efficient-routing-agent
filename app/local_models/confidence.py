def score(response):

    if len(response) > 80:
        return 0.92

    if len(response) > 40:
        return 0.80

    return 0.55