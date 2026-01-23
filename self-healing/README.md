# Self-Healing Engine
# Self-Healing Logic & Monitoring Module

This module implements the **Self-Healing Decision Engine** for the Cloud-Native AI-Powered WAF project.

It takes input from the AI/ML Detection Engine and automatically decides whether to:
- Log the event (WARN)
- Test a block without affecting users (SHADOW mode)
- Enforce a block rule on the WAF (BLOCK)

---

## 📌 Role of This Module

This module acts as the **bridge** between:
AI Detection Engine → WAF → Monitoring & Rollback

It ensures:
- Fast response to real attacks
- Safety using shadow mode
- Automatic rollback for false positives

---

## 🔁 Self-Healing Flow

1. WAF logs a suspicious request  
2. AI Engine analyzes the request  
3. AI sends:
   - `attack_type`
   - `confidence_score`
   - `source_ip`

4. Decision Engine:
   - If score < 0.50 → WARN
   - If score ≥ 0.50 and < 0.85 → SHADOW
   - If score ≥ 0.85 → BLOCK

5. If BLOCK → Rule is pushed to WAF  
6. Monitoring starts  
7. If error rate spikes → Rollback removes the rule  

---

## 🧠 Decision Engine Logic

File: `decision_engine.py`

The engine:
- Uses thresholds to classify severity
- Triggers appropriate WAF actions
- Logs all decisions for auditing

---

## 🪂 Rollback Logic

File: `rollback.py`

Rollback is triggered when:
- Too many users get blocked
- Error rate increases suddenly
- False positives are detected

It removes the last applied rule and restores normal traffic.

---

## 📊 Monitoring & Alerts

Monitoring tracks:
- Block count
- Error rate
- Request volume

Alerts can be:
- Console-based
- Email (conceptual)

---

## 🧪 Testing

Test scenarios are defined in:  
`docs/TESTING.md`

---

## 👤 Owner

Member 4 – Self-Healing Logic & Monitoring
