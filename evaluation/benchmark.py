import json
import time

from app.router.router import HybridRouter

router = HybridRouter()

with open("datasets/prompts.json", "r") as f:
    prompts = json.load(f)

results = []

for item in prompts:
    start = time.perf_counter()

    output = router.route(item["prompt"])

    elapsed = (time.perf_counter() - start) * 1000

    output["latency_ms"] = round(elapsed, 2)
    output["id"] = item["id"]

    results.append(output)

print("\n========== Benchmark ==========\n")

for r in results:
    print(f"Prompt {r['id']}")
    print(f"Model      : {r['model']}")
    print(f"Latency    : {r['latency_ms']} ms")
    print(f"Tokens     : {r['tokens']}")
    print(f"Confidence : {r['confidence']}")
    print("-" * 40)

with open("evaluation/reports/benchmark_results.json", "w") as f:
    json.dump(results, f, indent=4)

print("\nBenchmark completed.")