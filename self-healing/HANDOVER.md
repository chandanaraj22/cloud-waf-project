# Self-Healing Module – Handover Document

This document helps a new developer understand and continue the Self-Healing Logic module.

---

## 📌 What This Module Does

This module:
- Receives AI detection output
- Decides whether to WARN, SHADOW, or BLOCK
- Triggers WAF rule updates (via script/API call)
- Monitors impact
- Rolls back bad rules automatically

---

## 📂 Files in This Module

| File | Purpose |
|------|--------|
| decision_engine.py | Main logic for deciding actions |
| rollback.py | Handles undoing bad rules |
| README.md | Explains the design & flow |
| HANDOVER.md | This document |

---

## ▶ How to Run (Demo Mode)

You can simulate the module locally:

```bash
cd self-healing
python decision_engine.py
python rollback.py
