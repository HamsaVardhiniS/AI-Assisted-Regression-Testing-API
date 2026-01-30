def final_verdict(rule_results: dict, anomaly_scores):
    rule_fail = any(v["status"] == "FAIL" for v in rule_results.values())
    rule_warn = any(v["status"] == "WARN" for v in rule_results.values())

    # Isolation Forest heuristic
    anomaly_flag = anomaly_scores.mean() < -0.05

    if rule_fail or anomaly_flag:
        return "FAIL"
    elif rule_warn:
        return "WARN"
    else:
        return "PASS"
