import json

with open("evaluation/reports/benchmark_results.json") as f:
    data = json.load(f)

summary = {}

for item in data:
    model = item["model"]

    if model not in summary:
        summary[model] = {
            "count": 0,
            "tokens": 0,
            "latency": 0
        }

    summary[model]["count"] += 1
    summary[model]["tokens"] += item["tokens"]
    summary[model]["latency"] += item["latency_ms"]

print("\n===== Model Comparison =====\n")

for model, stats in summary.items():

    avg_tokens = stats["tokens"] / stats["count"]
    avg_latency = stats["latency"] / stats["count"]

    print(model)
    print("Requests :", stats["count"])
    print("Avg Tokens :", round(avg_tokens, 2))
    print("Avg Latency :", round(avg_latency, 2), "ms")
    print("-" * 40)