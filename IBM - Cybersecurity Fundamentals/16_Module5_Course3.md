# Responding to Cyberattacks: Frameworks, Testing, and Recovery  

---

## Learning Objectives  
By the end of this module, you will be able to:  
1. **Explain the six phases of the SANS Institute incident response framework**.  
2. **Describe three types of simulated exercises to test incident preparedness**.  
3. **Define business continuity and disaster recovery**.  

---

## 1. SANS Institute Incident Response Framework  
The SANS Institute outlines a six-phase approach to manage cybersecurity incidents effectively:  

| **Phase**               | **Description**                                                                 | **Key Activities**                                                                 |  
|-------------------------|---------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|  
| **1. Preparation**      | Build readiness before incidents occur.                                         | - Develop IR policies/playbooks.<br>- Train response teams.<br>- Deploy monitoring tools. |  
| **2. Identification**   | Detect and confirm incidents through alerts/logs.                                | - Analyze SIEM alerts.<br>- Interview stakeholders.<br>- Validate indicators of compromise (IoCs). |  
| **3. Containment**      | Limit damage by isolating affected systems.                                      | - Short-term: Disconnect infected devices.<br>- Long-term: Patch vulnerabilities. |  
| **4. Eradication**      | Remove threats and root causes from the environment.                            | - Delete malware.<br>- Rebuild compromised systems.                                |  
| **5. Recovery**         | Restore systems to normal operations safely.                                    | - Validate clean backups.<br>- Monitor for recurrence.                             |  
| **6. Lessons Learned**  | Review and improve the response process.                                        | - Document findings.<br>- Update playbooks.<br>- Share insights with stakeholders. |  

**Case Study**:  
A bank used the SANS framework to contain a ransomware attack:  
1. **Containment**: Isolated infected servers within 30 minutes.  
2. **Eradication**: Removed ransomware using CrowdStrike Falcon.  
3. **Recovery**: Restored data from immutable backups.  

---

## 2. Simulated Incident Preparedness Activities  
Organizations test readiness through three types of exercises:  

| **Exercise Type**          | **Description**                                                                 | **Example**                                      |  
|----------------------------|---------------------------------------------------------------------------------|--------------------------------------------------|  
| **Tabletop Exercises**      | Discussion-based drills to walk through hypothetical scenarios.                | Simulating a phishing campaign targeting executives. |  
| **Red Team/Blue Team**      | Offensive (Red Team) vs. defensive (Blue Team) mock attacks.                    | Red Team exploits a vulnerability; Blue Team detects/responds. |  
| **Full-Scale Simulations**  | Real-world scenario execution with minimal warning.                             | Simulating a multi-vector attack (ransomware + DDoS). |  

**Benefits**:  
- Identifies gaps in communication, tools, and processes.  
- Builds muscle memory for high-pressure situations.  

---

## 3. Business Continuity (BC) vs. Disaster Recovery (DR)  

| **Term**                | **Definition**                                                                 | **Focus**                                      | **Example**                                      |  
|-------------------------|---------------------------------------------------------------------------------|-----------------------------------------------|--------------------------------------------------|  
| **Business Continuity** | Ensures critical operations continue during/after a disruption.                 | Maintaining workflows (e.g., remote work capabilities). | Using cloud apps during a server outage.         |  
| **Disaster Recovery**   | Restores IT systems/data after a catastrophic event (natural disaster, cyberattack). | Technical recovery (backups, failover sites). | Restoring databases from offsite backups post-ransomware. |  

### Key Components  
- **BC**: Risk assessments, alternate workspaces, supply chain redundancy.  
- **DR**: Backup strategies (3-2-1 rule), RTO (Recovery Time Objective), RPO (Recovery Point Objective).  

---

## 4. Case Study: Coordinating Response and Recovery  
**Scenario**: A retailer faces a DDoS attack during Black Friday.  
- **Response**:  
  1. **Containment**: Redirect traffic via CDN (Cloudflare).  
  2. **Recovery**: Failover to backup servers (RTO: 1 hour).  
- **BC/DR**: Activated crisis communication plan to update customers via social media.  

---

## Key Takeaways  
1. The **SANS framework** provides a structured approach to incident management.  
2. **Simulations** expose weaknesses and build team confidence.  
3. **BC/DR plans** ensure operational resilience beyond technical recovery.  

---

### References  
1. SANS Institute. (2023). *Incident Handler’s Handbook*.  
2. NIST SP 800-84. (2023). *Guide to Test, Training, and Exercise Programs*.  
3. ISO 22301:2019. *Business Continuity Management Systems*.  
