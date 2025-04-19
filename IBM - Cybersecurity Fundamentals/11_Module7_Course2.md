# Technical Scanning: Techniques, Tools, and Network Reconnaissance  

---

## Learning Objectives  
By the end of this module, you will be able to:  
1. **Explain the purpose and outputs of common technical scanning techniques**.  
2. **Perform network reconnaissance using industry-standard scanning tools**.  

---

## 1. Purpose of Technical Scanning  
Technical scanning is the process of **systematically probing systems, networks, or applications** to:  
- Identify active devices and services.  
- Discover vulnerabilities and misconfigurations.  
- Map network architecture.  
- Assess security posture.  

---

## 2. Typical Technical Scanning Techniques  

| **Technique**            | **Purpose**                                                                 | **Information Provided**                                                                 |  
|---------------------------|-----------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|  
| **Port Scanning**         | Identify open ports and services running on a target.                       | List of open ports (e.g., TCP 80/HTTP), service versions, and protocols.                |  
| **Vulnerability Scanning**| Detect known vulnerabilities (e.g., unpatched software).                    | CVEs, risk scores (CVSS), and remediation advice (e.g., CVE-2023-1234: Apache vulnerability). |  
| **Network Mapping**       | Discover devices and visualize network topology.                            | IP addresses, device types (e.g., routers, IoT), and connections between nodes.         |  
| **OS Fingerprinting**     | Determine the operating system of a target device.                          | OS type (e.g., Windows 11, Linux Kernel 5.15), and architecture (x86, ARM).             |  
| **Banner Grabbing**       | Retrieve service banners to identify software versions.                     | Web server type (e.g., Apache 2.4.57), database versions (e.g., MySQL 8.0).            |  

---

## 3. Performing Network Reconnaissance  
### Step-by-Step Process  

1. **Define Scope**: Identify IP ranges, domains, or systems to scan (e.g., `192.168.1.0/24`).  
2. **Choose Tools**: Select tools based on objectives (e.g., `Nmap` for port scanning).  
3. **Execute Scans**:  
   ```bash
   # Basic Nmap port scan
   nmap -sV -O 192.168.1.1
   ```  
   - `-sV`: Service version detection.  
   - `-O`: OS fingerprinting.  
4. **Analyze Results**:  
   - Open ports, live hosts, and potential vulnerabilities.  
   - Prioritize risks (e.g., exposed database ports).  

---

## 4. Key Network Scanning Tools  

| **Tool**       | **Purpose**                                  | **Example Command**                                  | **Output**                                      |  
|----------------|---------------------------------------------|-----------------------------------------------------|------------------------------------------------|  
| **Nmap**       | Port scanning, OS detection, service discovery. | `nmap -sS -p 1-1000 10.0.0.1`                     | Lists open ports and services.                 |  
| **Nessus**     | Vulnerability scanning.                     | GUI-based scan of IP range for CVEs.                | Risk assessment report with CVSS scores.       |  
| **Wireshark**  | Packet capture and analysis.                | Capture traffic on `eth0` and filter for HTTP.       | Decrypted packets showing headers/payloads.    |  
| **Masscan**    | High-speed port scanning.                   | `masscan 10.0.0.0/24 --ports 0-65535`               | Rapid identification of open ports.            |  
| **Netcat**     | Banner grabbing, manual port probing.       | `nc -zv 10.0.0.1 22`                                | Confirms if SSH (port 22) is open.             |  

---

## 5. Case Study: Detecting an Exposed Database  
**Scenario**: A company’s internal network scan reveals port `3306` (MySQL) open to the public internet.  
- **Tool Used**: `Nmap` (`nmap -sV -p 3306 203.0.113.5`).  
- **Findings**: MySQL 5.7.34 with default credentials.  
- **Risk**: Unauthorized access to sensitive customer data.  
- **Resolution**: Restrict port access and enforce strong authentication.  

---

## 6. Best Practices for Ethical Scanning  
- **Obtain Authorization**: Never scan networks without explicit permission.  
- **Limit Impact**: Use rate-limiting (`-T3` in Nmap) to avoid disrupting services.  
- **Document Findings**: Share reports with stakeholders for remediation.  
- **Stay Legal**: Comply with laws like the Computer Fraud and Abuse Act (CFAA).  

---

## 7. Real-World Applications  
- **Penetration Testing**: Simulate attacks to find weaknesses.  
- **Incident Response**: Identify compromised systems during breaches.  
- **Compliance Audits**: Meet standards like PCI-DSS (e.g., quarterly vulnerability scans).  

---

## Conclusion  
Technical scanning is foundational for proactive cybersecurity. By combining tools like Nmap and Nessus with structured methodologies, organizations can uncover risks, harden defenses, and prevent breaches.  

---

### References  
1. Nmap Documentation. (2023). *Network Scanning Basics*.  
2. NIST SP 800-115. (2008). *Technical Guide to Information Security Testing*.  
3. MITRE ATT&CK. (2023). *Discovery Techniques (TA0007)*.  
