# Self-Healing Module – Test Scenarios

This document describes how the Self-Healing Logic reacts to different attack scenarios.

---

## 1. SQL Injection Attack

**Input (from AI Engine):**
```json
{
  "attack_type": "SQLi",
  "confidence_score": 0.92,
  "source_ip": "192.168.1.10"
}
