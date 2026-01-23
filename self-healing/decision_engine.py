"""
decision_engine.py

This module receives AI detection output and decides what action to take.
It supports:
- WARN (just log)
- SHADOW (test blocking without affecting users)
- BLOCK (enforce rule on WAF)

Member 4 – Self-Healing Logic
"""

import time
import json
from datetime import datetime


# Thresholds for decisions
WARN_THRESHOLD = 0.50
BLOCK_THRESHOLD = 0.85


def decide_action(attack_type, confidence_score):
    """
    Decide what action to take based on AI confidence score.
    """
    if confidence_score >= BLOCK_THRESHOLD:
        return "BLOCK"
    elif confidence_score >= WARN_THRESHOLD:
        return "SHADOW"
    else:
        return "WARN"


def trigger_waf_action(action, attack_type, source_ip):
    """
    Simulate pushing rule to WAF.
    In real system, this would call a script / API owned by WAF team.
    """
    event = {
        "time": datetime.utcnow().isoformat(),
        "ip": source_ip,
        "attack_type": attack_type,
        "action": action
    }

    print("[Self-Healing] Action Triggered:", json.dumps(event, indent=2))

    # Placeholder: In real life this would call WAF rule engine
    if action == "BLOCK":
        print(f"→ Blocking IP {source_ip} for {attack_type}")
    elif action == "SHADOW":
        print(f"→ Shadow-testing block for {source_ip}")
    else:
        print(f"→ Logging only for {source_ip}")


def process_ai_output(attack_type, confidence_score, source_ip):
    """
    Main entry point: Called when AI flags a request.
    """
    print("\n[AI → Self-Healing] Incoming Detection")
    print(f"Attack: {attack_type}, Score: {confidence_score}, IP: {source_ip}")

    action = decide_action(attack_type, confidence_score)
    print(f"[Decision Engine] Final Action: {action}")

    trigger_waf_action(action, attack_type, source_ip)


# Demo run
if __name__ == "__main__":
    # Simulated AI output
    test_events = [
        ("SQLi", 0.92, "192.168.1.10"),
        ("XSS", 0.70, "192.168.1.11"),
        ("Normal", 0.30, "192.168.1.12"),
    ]

    for attack, score, ip in test_events:
        process_ai_output(attack, score, ip)
        time.sleep(1)
