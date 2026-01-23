"""
rollback.py

This module handles rollback logic for self-healing.
If blocking causes issues (false positives / high error rate),
it will remove the rule and restore traffic.

Member 4 – Self-Healing Logic
"""

import time
from datetime import datetime


ROLLBACK_ERROR_THRESHOLD = 5   # simulate: 5 errors = rollback
BLOCK_MONITOR_WINDOW = 60      # seconds


def monitor_and_rollback(rule_id, error_count):
    """
    Simulate monitoring system health after a rule is applied.
    """
    print("\n[Rollback Engine] Monitoring rule:", rule_id)
    print(f"Current error count: {error_count}")

    if error_count >= ROLLBACK_ERROR_THRESHOLD:
        rollback_rule(rule_id)
    else:
        print("→ System healthy. No rollback needed.")


def rollback_rule(rule_id):
    """
    Simulate removing a bad rule from WAF.
    """
    event_time = datetime.utcnow().isoformat()
    print(f"\n[ROLLBACK TRIGGERED] {event_time}")
    print(f"→ Rolling back rule: {rule_id}")
    print("→ Restoring normal traffic flow")


# Demo
if __name__ == "__main__":
    test_rule = "auto_block_sqli_192.168.1.10"
    simulated_error_count = 7

    monitor_and_rollback(test_rule, simulated_error_count)
    time.sleep(1)
