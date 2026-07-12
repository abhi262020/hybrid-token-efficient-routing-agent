import json

with open("evaluation/reports/benchmark_results.json") as f:
    data = json.load(f)

total = 0

highest = 0

lowest = 999999

for item in data:

    tokens = item["tokens"]

    total += tokens

    highest = max(highest, tokens)

    lowest = min(lowest, tokens)

average = total / len(data)

print("\n===== Token Analysis =====\n")

print("Total Tokens :", total)
print("Average Tokens :", round(average, 2))
print("Highest :", highest)
print("Lowest :", lowest)