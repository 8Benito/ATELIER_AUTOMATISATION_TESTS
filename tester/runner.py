import datetime
from .tests import executer_tests

def p95(latencies):
    """Calcule le 95ème centile d'une liste de latences."""
    if not latencies: return 0
    latencies_tries = sorted(latencies)
    index = int(len(latencies_tries) * 0.95)
    return round(latencies_tries[index], 2)

def run_suite():
    timestamp = datetime.datetime.now().isoformat()
    tests_resultats = executer_tests()
    
    total = len(tests_resultats)
    passed = sum(1 for t in tests_resultats if t["status"] == "PASS")
    failed = total - passed
    error_rate = round(failed / total, 2) if total > 0 else 1.0
    
    # Extraction des latences réelles (exclusion des tests purement logiques à 0ms)
    latencies = [t["latency_ms"] for t in tests_resultats if t["latency_ms"] > 0]
    latency_avg = round(sum(latencies) / len(latencies), 2) if latencies else 0
    latency_p95 = p95(latencies)
    
    run_data = {
        "api": "Frankfurter",
        "timestamp": timestamp,
        "summary": {
            "passed": passed,
            "failed": failed,
            "error_rate": error_rate,
            "latency_ms_avg": latency_avg,
            "latency_ms_p95": latency_p95
        },
        "tests": tests_resultats
    }
    
    return run_data