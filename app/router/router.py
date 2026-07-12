from fastapi import HTTPException

from app.classifier.intent_classifier import classify
from app.classifier.complexity import estimate

from app.router.policy import choose_model
from app.router.escalation import next_model

from app.fireworks.client import FireworksClient

from app.validator.confidence import calculate_confidence
from app.validator.quality import validate_quality


class HybridRouter:

    def __init__(self):
        self.client = FireworksClient()

    def route(self, prompt: str):

        task = classify(prompt)
        complexity = estimate(prompt, task)

        model = choose_model(complexity)

        print("=" * 60)
        print("Initial Model :", model.name)
        print("Complexity    :", complexity)
        print("=" * 60)

        response = self.client.generate(model.name, prompt)

        if "choices" not in response:
            raise HTTPException(
                status_code=500,
                detail=response
            )

        answer = response["choices"][0]["message"]["content"]

        usage = response.get("usage", {})

        tokens = usage.get("total_tokens", 0)

        confidence = calculate_confidence(answer)
        quality = validate_quality(answer)

        if confidence < 0.85 or not quality:

            better_model = next_model(model.name)

            print("Escalating to:", better_model.name)

            if better_model.name != model.name:

                response = self.client.generate(
                    better_model.name,
                    prompt
                )

                if "choices" not in response:
                    raise HTTPException(
                        status_code=500,
                        detail=response
                    )

                answer = response["choices"][0]["message"]["content"]

                usage = response.get("usage", {})

                tokens = usage.get("total_tokens", tokens)

                confidence = calculate_confidence(answer)

                model = better_model

        return {
            "model": model.name,
            "task": task.value,
            "complexity": complexity,
            "confidence": round(confidence, 2),
            "tokens": tokens,
            "response": answer,
        }