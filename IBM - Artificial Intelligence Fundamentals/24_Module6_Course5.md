# Privacy in AI: Key Concepts and Techniques

## Personal Information vs. Sensitive Personal Information

### **Personal Information (PI)**  
Data that can identify an individual directly or indirectly.  

| Examples                  | Non-Examples               |  
|---------------------------|----------------------------|  
| Name, email, phone number | Aggregated age statistics  |  
| IP address, cookie IDs     | Publicly available data    |  
| Geolocation data          | Anonymized purchase trends |  

### **Sensitive Personal Information (SPI)**  
Subset of PI requiring stricter protection due to higher privacy risks.  

| Examples                          | Regulatory Context               |  
|-----------------------------------|-----------------------------------|  
| Racial/ethnic origin              | GDPR Article 9                   |  
| Health records, genetic data      | HIPAA (US healthcare)            |  
| Biometric data (e.g., fingerprints) | CCPA (California consumer privacy)|  
| Political/religious beliefs       | Brazil’s LGPD                    |  

---

## Model Anonymization Techniques  
Methods to strip data of identifiable markers while preserving utility.  

| Technique            | Description                                  | Use Case                   |  
|----------------------|----------------------------------------------|----------------------------|  
| **k-Anonymity**      | Ensure each record is indistinguishable from ≥k-1 others | Public health datasets |  
| **Pseudonymization** | Replace identifiers with reversible tokens (e.g., "User#XZY") | Clinical trials          |  
| **Synthetic Data**   | Generate artificial data mimicking real distributions | AI training           |  
| **Aggregation**      | Report group-level stats (e.g., averages)    | Marketing analytics       |  

**Limitation**: Re-identification risks persist if combined with external data.  

---

## Differential Privacy  
A mathematical framework to quantify and limit privacy loss when sharing data.  

- **Core Idea**: Add controlled noise to data/results to prevent identifying individuals.  
- **ε (Epsilon) Parameter**: Lower ε = stronger privacy guarantees (e.g., ε=0.1 vs. ε=5).  

**Example**:  
- A hospital shares pandemic data with researchers.  
- Differential privacy adds noise to case counts, ensuring no patient is identifiable.  

**Adoption**: Apple (iOS), US Census Bureau.  

---

## Data Minimization Principles  
Collect/retain only data essential for a specific purpose.  

| Principle              | Description                                  | Example                          |  
|------------------------|----------------------------------------------|----------------------------------|  
| **Purpose Limitation** | Collect data only for stated, explicit goals | E-commerce site avoids tracking political views |  
| **Storage Limitation** | Delete data after fulfilling its purpose     | Ride-sharing app purges trip logs after 6 months |  
| **Data Avoidance**     | Avoid collecting SPI unless absolutely needed | Survey skips questions about religion |  

---

## Case Study: Healthcare AI  
- **Challenge**: Train a diabetes prediction model without exposing patient records.  
- **Solution**:  
  1. **Anonymization**: Remove names/addresses; apply k-anonymity (k=10).  
  2. **Differential Privacy**: Add noise to glucose-level statistics (ε=0.5).  
  3. **Minimization**: Exclude non-essential data (e.g., employment history).  

---

## Ethical & Regulatory Implications  
- **GDPR Compliance**: Mandates anonymization/minimization (Articles 5, 25).  
- **Trust**: Transparent privacy practices increase user adoption.  
- **Bias Trade-offs**: Over-anonymization may reduce dataset diversity.  

---

> **Key Takeaway**: Balancing privacy and utility requires layered strategies:  
> **Minimize** → **Anonymize** → **Apply Differential Privacy**  

---

**Further Reading**:  
- [Differential Privacy in Practice (Google Research)](https://ai.googleblog.com/2020/05/opening-new-frontiers-with-duo-bard.html)  
- [GDPR Anonymization Guidelines](https://ec.europa.eu/info/law/law-topic/data-protection/reform/rules-business-and-organisations/de-identification/anonymisation_en)  
