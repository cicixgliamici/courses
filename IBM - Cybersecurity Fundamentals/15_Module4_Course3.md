# Detecting Cyberattacks: Methods and Practical Malware Scanning  

---

## Learning Objectives  
By the end of this module, you will be able to:  
1. **Describe common methods organizations use to detect cyberattacks**.  
2. **Run an on-demand antimalware scan using Malwarebytes**.  

---

## 1. Methods to Detect Cyberattacks  

### A. **Intrusion Detection Systems (IDS)**  
- **Purpose**: Monitor network traffic for suspicious patterns (e.g., port scanning, SQL injection).  
- **Types**:  
  - **Network IDS (NIDS)**: Analyzes traffic across the network (e.g., Snort, Suricata).  
  - **Host IDS (HIDS)**: Monitors activity on individual devices (e.g., file changes, registry edits).  

### B. **Security Information and Event Management (SIEM)**  
- **Purpose**: Aggregates and analyzes logs from multiple sources (firewalls, servers, endpoints) to identify anomalies.  
- **Examples**: Splunk, Microsoft Sentinel, Elastic Security.  
- **Use Case**: Correlating failed login attempts across systems to detect brute-force attacks.  

### C. **Endpoint Detection and Response (EDR)**  
- **Purpose**: Continuously monitors endpoints (laptops, servers) for malicious activity.  
- **Features**: Behavioral analysis, threat hunting, automated response.  
- **Examples**: CrowdStrike Falcon, Microsoft Defender for Endpoint.  

### D. **User and Entity Behavior Analytics (UEBA)**  
- **Purpose**: Uses machine learning to detect deviations from normal behavior (e.g., unusual data access times).  
- **Example**: A user downloading 10GB of files at 3 AM triggers an alert.  

### E. **Threat Intelligence Feeds**  
- **Purpose**: Integrates real-time data on known malicious IPs, domains, and file hashes.  
- **Tools**: MISP, AlienVault OTX, commercial feeds (e.g., FireEye).  

### F. **Honeypots/Decoys**  
- **Purpose**: Fake systems designed to lure attackers and study their tactics.  
- **Example**: Deploying a mock database server to detect reconnaissance activity.  

---

## 2. Running an On-Demand Antimalware Scan with Malwarebytes  

### Step 1: Install Malwarebytes  
- Download from [malwarebytes.com](https://www.malwarebytes.com/).  
- Follow installation prompts (ensure real-time protection is enabled).  

### Step 2: Perform a Manual Scan  
1. **Open Malwarebytes**.  
2. Navigate to the **Dashboard** > **Scan** tab.  
3. Choose a scan type:  
   - **Threat Scan**: Quick check for common threats.  
   - **Full Scan**: Deep analysis of all files and processes.  
   - **Custom Scan**: Target specific folders (e.g., downloads directory).  

4. **Click Scan Now**.  
   ```plaintext
   Example Output:
   - 12 files scanned.
   - 2 threats detected: Trojan.Emotet, PUP.Optional.Adware.
   ```  

5. **Quarantine or Remove Threats**:  
   - Review results and select **Quarantine** to isolate malicious files.  
   - Reboot if prompted.  

### Step 3: Schedule Regular Scans  
- Enable **Automatic Scans** in Settings > Scan Schedule.  

---

## 3. Case Studies: Attack Detection in Action  

### A. **SolarWinds Hack Detection (2020)**  
- **Method**: Anomalous network traffic from Orion software updates.  
- **Tool**: FireEye’s Red Team tools detected unauthorized access.  

### B. **Ransomware Detection via EDR**  
- **Scenario**: A healthcare provider’s EDR flagged unusual file encryption patterns.  
- **Result**: Contained the attack before critical systems were compromised.  

---

## 4. Challenges in Attack Detection  
- **False Positives**: Legitimate activity mistaken for threats (e.g., admin bulk data transfers).  
- **Encrypted Traffic**: Hinders NIDS analysis without decryption capabilities.  
- **Slow Detection**: Average breach takes **287 days** to identify ([IBM, 2023](https://www.ibm.com/reports/data-breach)).  

---

## 5. Key Takeaways  
1. **Layered Detection**: Combine IDS, SIEM, and EDR for comprehensive coverage.  
2. **Proactive Scanning**: Tools like Malwarebytes catch threats before they escalate.  
3. **Behavioral Analysis**: UEBA and threat hunting uncover stealthy attacks.  

---

### References  
1. NIST SP 800-94. (2023). *Guide to Intrusion Detection and Prevention Systems*.  
2. MITRE ATT&CK. (2023). *Detection Techniques*.  
3. Malwarebytes. (2023). *User Guide for Scanning*.  
4. IBM. (2023). *Cost of a Data Breach Report*.  
