import csv

WEIGHTS = {"C1": 25, "C2": 25, "C3": 20, "C4": 20, "C5": 10}
TIE_BREAK = ["C2", "C3", "C4", "C1", "C5"]

with open("SCORE_MATRIX.csv", encoding="utf-8-sig", newline="") as f:
    rows = list(csv.DictReader(f))

for row in rows:
    total = sum(float(row[c]) / 5 * WEIGHTS[c] for c in WEIGHTS)
    if abs(total - float(row["score"])) > 1e-9:
        raise SystemExit(f"Score mismatch {row['candidate']}: {total} != {row['score']}")

ordered = sorted(
    rows,
    key=lambda row: (
        -float(row["score"]),
        *(-float(row[c]) for c in TIE_BREAK),
        row["candidate"].casefold(),
    ),
)

for position, row in enumerate(ordered, 1):
    if int(row["rank"]) != position:
        raise SystemExit(f"Rank mismatch {row['candidate']}: {row['rank']} != {position}")

print("PASS", len(ordered), "participants")
