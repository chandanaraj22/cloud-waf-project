# Cloud-Based AI-Driven Self-Healing Web Application Firewall (WAF)

---

## 1. Purpose of This Document

This document defines the frozen, high-level architecture of the Cloud-Based AI-Driven Self-Healing WAF system.

It serves to:
- Remove ambiguity across team members
- Clearly define system components and responsibilities
- Establish system boundaries and scope
- Act as a single source of truth before implementation begins

Once finalized, this architecture must not change without team-wide agreement.

---

## 2. High-Level System Overview

The system is designed to protect a web application by inspecting incoming traffic using a Web Application Firewall (WAF) and enhancing detection capabilities through AI-based anomaly detection.

The architecture follows a layered security approach:
- Traffic inspection and filtering
- Centralized logging (file-based)
- AI-based anomaly detection
- Automated mitigation and response

The system is deployed on **Oracle Cloud Infrastructure (OCI – Always Free tier)** to ensure feasibility for live implementation.

---

## 3. Core Components

### 3.1 Client (User / Attacker)

- Generates HTTP/HTTPS requests
- Can represent legitimate users or malicious actors
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
- Blocks known attack patterns such as SQL injection and XSS

Blocked traffic is denied immediately. Allowed traffic proceeds to the application.

---

### 3.3 Application Layer (Demo App)

- A simple Flask-based web application
- Represents a protected backend service
- Used to simulate realistic web traffic
- Does not contain business-critical logic

The application itself does not implement security mechanisms.

---

### 3.4 Logging Layer (File-Based)

Traffic and security events are logged for visibility and analysis.

**Logging Sources**
- NGINX access logs
- ModSecurity audit logs
- Application logs (optional)

**Log Storage**
- Local file-based logs on the server
- Logs are structured to enable parsing by the AI engine

**Optional Enhancement**
- ELK-lite stack may be used for visualization purposes only
- ELK is not required for core system functionality

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

The AI engine does not directly block traffic. It produces detection insights for the response engine.

---

### 3.6 Automation & Response Engine

This component enables the system to be self-healing.

**Responsibilities**
- Receive anomaly alerts from the AI engine
- Decide appropriate mitigation actions
- Automatically enforce responses

**Example Actions**
- Block suspicious IP addresses
- Dynamically update ModSecurity rules
- Log response actions for audit and review

This component closes the feedback loop between detection and protection.

---

## 4. End-to-End Traffic Flow

1. Client sends an HTTP/HTTPS request  
2. Request enters NGINX (reverse proxy)  
3. ModSecurity inspects the request  
   - If malicious → request is blocked  
   - If allowed → forwarded to the application  
4. Application processes the request and responds  
5. Logs are generated at the WAF and application layers  
6. Logs are written to local log files  
7. AI engine analyzes logs for anomalies  
8. If an anomaly is detected:  
   - Response engine triggers mitigation  
   - WAF rules or IP blocks are updated  

---

## 5. Architecture Principles

- **Defense in Depth:** Multiple layers of protection
- **Separation of Concerns:** Each component has a single responsibility
- **Simplicity:** Focus on reliable, demonstrable functionality
- **Automation First:** Minimize manual intervention
- **Explainability:** Clear detection and response logic

---

## 6. Out of Scope (Explicitly Excluded)

The following are intentionally excluded from this project:
- Production-grade enterprise WAF deployment
- Deep learning or complex neural networks
- User authentication and authorization
- Compliance certifications (PCI-DSS, ISO)
- High-availability or multi-region failover
- Full-scale SIEM or SOAR platforms

---

## 7. Assumptions

- The system runs in a controlled cloud environment
- Traffic volume is moderate and suitable for experimentation
- AI models are trained on representative log data
- Automated actions are limited to non-destructive mitigations
- The project prioritizes deployability and live demonstration

---

## 8. Future Enhancements (Not Implemented)

- Real-time streaming detection
- Advanced visualization dashboards
- Integration with SOAR platforms
- Threat intelligence feed integration
- Adaptive response tuning

---

## 9. Architecture Freeze Declaration (FINAL)

This document represents the **final frozen system architecture** for the capstone project.

The following components are frozen:
- Cloud Provider: Oracle Cloud Infrastructure (OCI – Always Free)
- WAF: NGINX + ModSecurity
- Application: Flask demo application
- AI Model: Isolation Forest (Python)
- Logging: File-based WAF and application logs (ELK-lite optional)
- Automation: IP blocking and dynamic WAF rule updates

Any changes to core components, data flow, or technology choices must be reviewed and approved by all team members.
