from app.local_models.loader import generator


def generate(prompt):

    output = generator(
        prompt,
        max_new_tokens=128
    )

    return output[0]["generated_text"]