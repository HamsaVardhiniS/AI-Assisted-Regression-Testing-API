import pandas as pd
import json

FEATURES = [
    "Air temperature [K]",
    "Process temperature [K]",
    "Rotational speed [rpm]",
    "Torque [Nm]",
    "Tool wear [min]"
]

def build_baseline(csv_path: str, output_path: str):
    df = pd.read_csv(csv_path)

    # Define golden baseline (healthy operation)
    baseline_df = df[
        (df["Machine failure"] == 0) &
        (df["TWF"] == 0) &
        (df["Tool wear [min]"] < 50)
    ]

    stats = {}
    for col in FEATURES:
        stats[col] = {
            "mean": float(baseline_df[col].mean()),
            "std": float(baseline_df[col].std())
        }

    with open(output_path, "w") as f:
        json.dump(stats, f, indent=4)

    return baseline_df[FEATURES]
