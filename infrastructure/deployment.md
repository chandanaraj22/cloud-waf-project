# Cloud & Infrastructure Deployment (OCI)

## Project
Cloud-Based AI-Driven Self-Healing WAF

## Cloud Platform
Oracle Cloud Infrastructure (OCI) – Always Free Tier

## Deployment Overview
The system is deployed on a single OCI Virtual Machine running Ubuntu.
Docker is used to host all components as containers.

## OCI Components Used

### 1. OCI Compute Instance (VM)
- Ubuntu Linux Virtual Machine
- Hosts Docker and Docker Compose
- Runs NGINX and Flask containers

### 2. Networking
- Virtual Cloud Network (VCN)
- Public Subnet
- Security Rules:
  - Allow HTTP (Port 80)
  - Allow HTTPS (Port 443)
  - Restrict SSH (Port 22) to developer IP

## Traffic Flow
Internet → NGINX (WAF Entry Point) → Flask Application

1. Client sends HTTP request from browser
2. Request reaches OCI VM public IP
3. NGINX container receives request on port 80
4. NGINX forwards request to Flask app container
5. Response is sent back to client via NGINX

## Logging
- NGINX access and error logs are generated inside the container
- Logs are stored on the VM filesystem
- These logs will be used by AI engine in later phases

## Outcome (Week-1)
- End-to-end traffic pipeline established
- Application accessible only via NGINX
- Infrastructure ready for WAF and security extensions
