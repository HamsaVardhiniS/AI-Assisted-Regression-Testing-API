from fastapi import FastAPI, UploadFile
import pandas as pd
import json
import joblib

from baseline.baseline_builder import build_baseline
from regression.anomaly_model import train_model, score_samples
from regression.rule_checks import check_drift
from regression.verdict_engine import final_verdict

FEATURES = [
    "Air temperature [K]",
    "Process temperature [K]",
    "Rotational speed [rpm]",
    "Torque [Nm]",
    "Tool wear [min]"
]

app = FastAPI(title="Regression Quality Monitor")

@app.post("/baseline/create")
def create_baseline():
    baseline_data = build_baseline(
        "data/ai4i.csv",
        "baseline/baseline_stats.json"
    )

    train_model(
        baseline_data,
        "models/isolation_forest.pkl"
    )

    return {"status": "Baseline statistics and model created successfully"}

@app.post("/regression/check")
def regression_check(file: UploadFile):
    df = pd.read_csv(file.file)

    with open("baseline/baseline_stats.json") as f:
        baseline_stats = json.load(f)

    model = joblib.load("models/isolation_forest.pkl")

    current_df = df[FEATURES]

    rule_results = check_drift(baseline_stats, current_df)
    anomaly_scores = score_samples(model, current_df)

    verdict = final_verdict(rule_results, anomaly_scores)

    return {
        "verdict": verdict,
        "rule_analysis": rule_results,
        "avg_anomaly_score": round(float(anomaly_scores.mean()), 4)
    }
