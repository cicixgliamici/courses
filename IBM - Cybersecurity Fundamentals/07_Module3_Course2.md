# Structure of a Cyberattack: Cyber Kill Chain and MITRE ATT&CK  
*From Planning to Execution – A Tactical Breakdown*  

---

## Learning Objectives  
By the end of this module, you will be able to:  
1. **Explain the stages of a cyberattack using the Cyber Kill Chain framework**.  
2. **Apply the Cyber Kill Chain to a real-world attack scenario**.  
3. **Map attacker tactics and techniques using the MITRE ATT&CK matrix**.  

---

## 1. The Cyber Kill Chain Framework  
Developed by Lockheed Martin, the **Cyber Kill Chain** defines seven stages of a cyberattack:  

| **Stage**               | **Description**                                                                 |  
|-------------------------|---------------------------------------------------------------------------------|  
| **1. Reconnaissance**   | Attacker researches targets (e.g., email scraping, network scanning).          |  
| **2. Weaponization**    | Creates malicious tools (e.g., malware-laced documents, exploit code).         |  
| **3. Delivery**         | Transfers weapon to target (e.g., phishing email, compromised website).        |  
| **4. Exploitation**     | Triggers vulnerability to execute code (e.g., buffer overflow, macro exploit).  |  
| **5. Installation**     | Deploys persistent access (e.g., backdoor, ransomware payload).                |  
| **6. Command & Control (C2)** | Establishes communication with attacker’s server.                             |  
| **7. Actions on Objectives** | Achieves goals (e.g., data theft, encryption, sabotage).                     |  

---

## 2. Applying the Cyber Kill Chain: A Ransomware Scenario  
**Scenario**: Attackers deploy ransomware on a hospital network.  

| **Stage**               | **Attacker Actions**                                                           |  
|-------------------------|---------------------------------------------------------------------------------|  
| **Reconnaissance**      | Scrape hospital employee emails from LinkedIn; identify outdated VPN software.  |  
| **Weaponization**       | Embed ransomware (e.g., Ryuk) into a fake "COVID-19 Safety Guidelines" PDF.     |  
| **Delivery**            | Send phishing emails to hospital staff with the malicious attachment.          |  
| **Exploitation**        | Exploit a VPN vulnerability (CVE-2023-1234) to bypass authentication.           |  
| **Installation**        | Deploy ransomware across networked systems using PsExec.                        |  
| **C2**                  | Ransomware connects to attacker’s Tor-based server for decryption keys.         |  
| **Actions on Objectives** | Encrypt patient records; demand $5 million in Bitcoin.                        |  

**Outcome**: Hospital operations halted for 72 hours; data leaked after ransom refusal.  

---

## 3. Mapping to MITRE ATT&CK Matrix  
The **MITRE ATT&CK** matrix categorizes attacker tactics, techniques, and sub-techniques. Below is the ransomware attack mapped to ATT&CK:  

| **MITRE Tactics**       | **Techniques (Examples)**                                 | **Scenario Application**                          |  
|-------------------------|-----------------------------------------------------------|---------------------------------------------------|  
| **Reconnaissance**      | T1595: Active Scanning                                    | Scanning hospital’s VPN for vulnerabilities.      |  
| **Initial Access**      | T1566: Phishing                                           | Malicious PDF sent via email.                     |  
| **Execution**           | T1204: User Execution                                     | Employee opens the infected PDF.                  |  
| **Persistence**         | T1547: Boot or Logon Autostart Execution                  | Ransomware adds itself to startup scripts.        |  
| **Privilege Escalation**| T1068: Exploitation for Privilege Escalation              | Exploiting VPN vulnerability for admin access.    |  
| **Defense Evasion**     | T1027: Obfuscated Files or Information                    | Encrypting ransomware payload to evade AV.        |  
| **Lateral Movement**    | T1021: Remote Services (PsExec)                           | Spreading ransomware across networked systems.    |  
| **Impact**              | T1486: Data Encrypted for Impact                          | Encrypting patient records.                       |  

---

## Case Study: SolarWinds Hack (2020)  
### Cyber Kill Chain Application:  
1. **Reconnaissance**: Identified SolarWinds as a software vendor with high-level client access.  
2. **Weaponization**: Injected Sunburst malware into Orion software updates.  
3. **Delivery**: Legitimate update pushed to 18,000+ customers.  
4. **Exploitation**: Exploited SAML token vulnerabilities to impersonate users.  
5. **Installation**: Established backdoors in target networks (e.g., U.S. government agencies).  
6. **C2**: Communicated with attacker-controlled domains.  
7. **Actions**: Exfiltrated sensitive data over months.  

### MITRE ATT&CK Mapping:  
- **Supply Chain Compromise (T1195)**  
- **Golden SAML Attack (T1606)**  

---

## Key Takeaways  
1. The **Cyber Kill Chain** helps defenders anticipate and disrupt attacks at early stages (e.g., blocking phishing in Delivery).  
2. **MITRE ATT&CK** provides granular insights into attacker behavior, improving detection rules and threat hunting.  
3. Real-world attacks often combine multiple tactics (e.g., phishing + privilege escalation).  

---

### References  
1. Lockheed Martin. (2011). *The Cyber Kill Chain*.  
2. MITRE ATT&CK Framework. (2023). *Enterprise Matrix*.  
3. CrowdStrike. (2023). *Global Threat Report – Ransomware Trends*.  
