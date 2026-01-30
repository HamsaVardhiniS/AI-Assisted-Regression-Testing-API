# AI-Assisted Regression Testing API

A production-style regression testing system that validates manufacturing telemetry against golden baselines using statistical drift checks and ML-based anomaly detection.

## Features

- Golden baseline construction from healthy machine runs
- Statistical drift detection (mean & variance)
- Isolation Forest anomaly detection
- PASS / WARN / FAIL verdict engine
- FastAPI-based deployment

## Tech Stack

- Python
- FastAPI
- Pandas, NumPy
- Scikit-learn
- Uvicorn

## Endpoints

### Create Baseline

POST /baseline/create  
Builds statistical baselines and trains anomaly detection model.

### Run Regression Check

POST /regression/check  
Uploads a CSV and returns regression verdict with diagnostics.

## How to Run

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app:app --reload
```
