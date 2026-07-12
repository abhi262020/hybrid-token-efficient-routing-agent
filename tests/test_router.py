from app.router.router import HybridRouter


def test_router():

    router = HybridRouter()

    result = router.route(
        "Explain Machine Learning."
    )

    assert isinstance(result, dict)

    assert "model" in result
    assert "response" in result
    assert "tokens" in result
    assert "confidence" in result