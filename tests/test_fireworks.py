from app.fireworks.client import FireworksClient


def test_connection():

    client = FireworksClient()

    result = client.generate(
        "accounts/fireworks/models/llama-v3p1-8b-instruct",
        "Hello!"
    )

    assert result is not None

    if isinstance(result, dict):
        print(result)
    else:
        print("Fireworks API Working")