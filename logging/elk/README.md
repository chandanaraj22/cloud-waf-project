This folder contains configuration related to the ELK stack.
ELK is used for log ingestion, indexing, visualization, and analysis.

# CloudWatch Monitoring – Self-Healing WAF

This document explains how monitoring and alerts would work using a cloud-native approach
(similar to AWS CloudWatch / OCI Monitoring).

---

## 📌 What We Monitor

Key metrics for self-healing:

- Request count
- Blocked IP count
- Error rate (4xx / 5xx)
- Latency / response time

---

## 🔄 Metric Flow

1. WAF and Self-Healing modules generate logs  
2. Logs are pushed to a cloud monitoring service  
3. Metrics are extracted and stored  
4. Dashboards show system health  

---

## 🔔 Alerts

Alerts are triggered when:

- Error rate > threshold  
- Block count spikes  
- Latency suddenly increases  

Alerts notify:
- Admin / Security Team
- System logs

---

## 🛡 Role in Self-Healing

Monitoring helps:
- Detect false positives
- Trigger rollback logic
- Ensure system stability

---

## 👤 Owner

Member 4 – Monitoring & Self-Healing
