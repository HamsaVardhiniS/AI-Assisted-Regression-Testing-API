def check_drift(baseline_stats: dict, current_df):
    results = {}

    for col, stats in baseline_stats.items():
        baseline_mean = stats["mean"]
        baseline_var = stats["std"] ** 2

        current_mean = current_df[col].mean()
        current_var = current_df[col].var()

        mean_drift = abs(current_mean - baseline_mean) / baseline_mean
        var_drift = abs(current_var - baseline_var) / baseline_var

        if mean_drift > 0.10 or var_drift > 0.20:
            status = "FAIL"
        elif mean_drift > 0.05:
            status = "WARN"
        else:
            status = "PASS"

        results[col] = {
            "mean_drift_pct": round(mean_drift * 100, 2),
            "variance_drift_pct": round(var_drift * 100, 2),
            "status": status
        }

    return results
