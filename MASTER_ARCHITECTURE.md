# MASTER ARCHITECTURE DOCUMENT  
Cloud-Based AI-Driven Self-Healing Web Application Firewall (WAF)

---

## 1. Purpose of This Document

This document defines the frozen, high-level architecture of the Cloud-Based AI-Driven Self-Healing WAF system.

It serves to:
- Remove ambiguity across team members
- Clearly define system components and responsibilities
- Establish system boundaries and scope
- Act as a single source of truth before implementation begins

Once finalized, this architecture should not change without team-wide agreement.

---

## 2. High-Level System Overview

The system is designed to protect a web application by inspecting incoming traffic using a Web Application Firewall (WAF) and enhancing detection capabilities through AI-based anomaly detection.

The architecture follows a layered security approach:
1. Traffic inspection and filtering
2. Centralized logging and monitoring
3. AI-based anomaly detection
4. Automated mitigation and response

The system is deployed on cloud infrastructure (AWS preferred).

---

## 3. Core Components

### 3.1 Client (User / Attacker)

- Generates HTTP/HTTPS requests
- Can be legitimate users or malicious actors
- Traffic enters the system through the WAF layer

---

### 3.2 WAF Layer (NGINX + ModSecurity)

**NGINX**
- Acts as a reverse proxy
- Serves as the entry point for all incoming traffic
- Forwards validated traffic to the backend application

**ModSecurity**
- Integrated with NGINX
- Inspects HTTP requests and responses
- Applies predefined and custom security rules
- Blocks known attack patterns (SQLi, XSS, etc.)

Blocked traffic is denied immediately. Allowed traffic proceeds to the application.

---

### 3.3 Application Layer (Demo App)

- A simple Flask-based web application
- Represents a protected backend service
- Used only to simulate realistic web traffic
- Does not contain business-critical logic

The application itself does not implement security logic.

---

### 3.4 Logging and Monitoring Layer

Traffic and security events are logged for visibility and analysis.

**Logging Sources**
- NGINX access logs
- ModSecurity audit logs
- Application logs (optional)

**Log Destinations**
- ELK Stack (Elasticsearch, Logstash, Kibana)
- AWS CloudWatch (alternative or complementary)

Logs are structured and stored for further processing by the AI engine.

---

### 3.5 AI Engine (Anomaly Detection)

The AI engine enhances traditional WAF capabilities by detecting unknown or zero-day attack patterns.

**Responsibilities**
- Parse and preprocess traffic logs
- Train machine learning models using historical data
- Detect anomalies in incoming traffic patterns

**Technology**
- Language: Python
- Model: Isolation Forest
- Approach: Unsupervised anomaly detection

The AI engine does not block traffic directly. It only generates detection insights.

---

### 3.6 Automation & Response Engine

This component enables the system to be “self-healing”.

**Responsibilities**
- Receive anomaly alerts from the AI engine
- Decide mitigation actions
- Automatically enforce responses

**Example Actions**
- Block suspicious IP addresses
- Update ModSecurity rules
- Trigger alerts or logs for manual review

This layer closes the feedback loop between detection and protection.

---

## 4. End-to-End Traffic Flow

1. Client sends HTTP/HTTPS request
2. Request enters NGINX (reverse proxy)
3. ModSecurity inspects request
   - If malicious → request blocked
   - If allowed → forwarded to application
4. Application processes request and responds
5. Logs generated at WAF and application layers
6. Logs sent to ELK / CloudWatch
7. AI engine analyzes logs for anomalies
8. If anomaly detected:
   - Response engine triggers mitigation
   - WAF configuration or rules are updated

---

## 5. Architecture Principles

- **Defense in Depth**: Multiple layers of protection
- **Separation of Concerns**: Each component has a single responsibility
- **Scalability**: Components can be scaled independently
- **Automation First**: Minimize manual intervention
- **Explainability**: Clear detection and response logic

---

## 6. Out of Scope (Explicitly Excluded)

The following are intentionally excluded from this project:
- Production-grade enterprise WAF deployment
- Deep learning or complex neural networks
- User authentication and authorization
- Compliance certifications (PCI-DSS, ISO)
- High-availability or multi-region failover

---

## 7. Assumptions

- The system runs in a controlled cloud environment
- Traffic volume is moderate and suitable for experimentation
- AI models are trained on representative log data
- Automated actions are limited to non-destructive mitigations

---

## 8. Future Enhancements (Not Implemented)

- Real-time streaming detection
- Reinforcement learning-based response tuning
- Integration with SOAR platforms
- Advanced threat intelligence feeds
- Dashboard-based response controls

---

## 9. Architecture Freeze Declaration

This document represents the frozen system architecture for Week 0.

Any changes to:
- Core components
- Data flow
- Technology choices

must be reviewed and approved by all team members.

---

