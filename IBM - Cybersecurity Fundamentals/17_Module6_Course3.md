# Introducing Cryptography: Foundations and Future Challenges  

---

## Learning Objectives  
By the end of this module, you will be able to:  
1. **Define cryptography**.  
2. **Explain the three properties of secure, reliable communications**.  
3. **Contrast symmetric and asymmetric encryption**.  
4. **Order the steps of asymmetric encryption**.  
5. **Describe the potential impact of quantum computing on cybersecurity**.  

---

## 1. What is Cryptography?  
**Definition**:  
Cryptography is the practice of securing information by transforming it (**encryption**) into an unreadable format, ensuring only authorized parties can decode it (**decryption**).  

**Purpose**:  
- **Confidentiality**: Keep data secret.  
- **Integrity**: Ensure data isn’t altered.  
- **Authenticity**: Verify sender/receiver identity.  

**Example**:  
HTTPS uses cryptography to protect web traffic between your browser and a server.  

---

## 2. Three Properties of Secure, Reliable Communications  

| **Property**         | **Description**                                                                 | **Cryptographic Tool**                          |  
|-----------------------|---------------------------------------------------------------------------------|------------------------------------------------|  
| **Confidentiality**  | Data is accessible only to authorized parties.                                  | Encryption (AES, RSA).                         |  
| **Integrity**        | Data remains unaltered during transmission.                                    | Hash functions (SHA-256), digital signatures.  |  
| **Authenticity**     | Parties can verify each other’s identities.                                    | Digital certificates (X.509), HMAC.            |  

**Example**:  
A digitally signed email ensures the sender is genuine (**authenticity**) and the content is unchanged (**integrity**).  

---

## 3. Symmetric vs. Asymmetric Encryption  

| **Aspect**            | **Symmetric Encryption**                         | **Asymmetric Encryption**                      |  
|------------------------|-------------------------------------------------|------------------------------------------------|  
| **Keys**              | Single shared key (e.g., AES-256).              | Public/private key pair (e.g., RSA-2048).      |  
| **Speed**             | Fast (suitable for bulk data).                  | Slow (used for small data like keys).          |  
| **Key Management**    | Challenging (secure key exchange required).     | Easier (public keys can be freely shared).     |  
| **Use Cases**         | Encrypting files, databases.                    | SSL/TLS, digital signatures, key exchange.     |  

**Example**:  
- **Symmetric**: Encrypting a hard drive with BitLocker (AES).  
- **Asymmetric**: Securing a website with HTTPS (RSA for key exchange, AES for data).  

---

## 4. Steps of Asymmetric Encryption  

1. **Key Generation**: Create a public/private key pair (e.g., using RSA).  
2. **Public Key Sharing**: The sender obtains the recipient’s public key.  
3. **Encryption**: The sender encrypts data with the recipient’s **public key**.  
4. **Transmission**: Encrypted data is sent over a network.  
5. **Decryption**: The recipient decrypts the data with their **private key**.  

**Diagram**:  
```plaintext
Sender → [Data + Public Key] → Encrypted Data → Recipient → [Encrypted Data + Private Key] → Decrypted Data
```

---

## 5. Quantum Computing’s Impact on Cybersecurity  

### Risks  
- **Break Classical Encryption**: Quantum algorithms like **Shor’s algorithm** can factor large primes, breaking RSA and ECC.  
- **Hash Vulnerabilities**: Grover’s algorithm reduces brute-force attack time for symmetric keys (halving effective key length).  

### Mitigations  
- **Post-Quantum Cryptography**: Algorithms resistant to quantum attacks (e.g., NIST’s CRYSTALS-Kyber, SPHINCS+).  
- **Quantum Key Distribution (QKD)**: Uses quantum physics to securely exchange keys (e.g., BB84 protocol).  

**Example**:  
A bank migrates from RSA to CRYSTALS-Kyber to protect customer transactions from future quantum threats.  

---

## Case Study: Hybrid Cryptography in Practice  
**TLS 1.3 Protocol**:  
- Uses **asymmetric encryption** (RSA/ECC) to exchange a symmetric key.  
- Uses **symmetric encryption** (AES-GCM) to encrypt session data.  
- Prepares for quantum threats by testing post-quantum algorithms.  

---

## Key Takeaways  
1. Cryptography ensures **confidentiality, integrity, and authenticity**.  
2. **Symmetric** and **asymmetric** encryption serve complementary roles.  
3. Quantum computing threatens current standards but drives innovation in **post-quantum cryptography**.  

---

### References  
1. NIST. (2023). *Post-Quantum Cryptography Standardization*.  
2. RSA Laboratories. (2023). *Public-Key Cryptography Standards*.  
3. Shor, P. (1994). *Algorithms for Quantum Computation*.  
