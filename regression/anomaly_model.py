from sklearn.ensemble import IsolationForest
import joblib

def train_model(baseline_data, model_path: str):
    model = IsolationForest(
        n_estimators=200,
        contamination=0.05,
        random_state=42
    )
    model.fit(baseline_data)
    joblib.dump(model, model_path)

def score_samples(model, data):
    """
    Higher score = more normal
    Lower (negative) score = more anomalous
    """
    return model.decision_function(data)
