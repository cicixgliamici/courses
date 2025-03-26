# TCP/IP Protocol Suite Course

## Course Overview
This course explores the TCP/IP protocol stack using a **top-down approach**:
1. **Application Layer**: HTTP, FTP
2. **Transport Layer**: TCP vs UDP
3. **Internet Layer**: IPv4 fundamentals
4. **Supplemental IP Services**

---

## Application Layer Protocols
### Core Concept
- Applications exchange **messages** using standardized protocols
- Both ends must implement the **same protocol** for successful communication

---

### HTTP (Hypertext Transfer Protocol)
| Feature          | Description                                                                 |
|------------------|-----------------------------------------------------------------------------|
| **Purpose**      | Web page transfer (text/hyperlinks)                                         |
| **Security**     | HTTPS adds TLS/SSL encryption                                               |
| **Model**        | Client-server request-response                                             |
| **Port**         | 80 (HTTP), 443 (HTTPS)                                                      |
| **Message Flow** | Client → Request → Server → Response (HTML/CSS/JS) → Client                 |

---

### FTP (File Transfer Protocol)
| Feature          | Description                                                                 |
|------------------|-----------------------------------------------------------------------------|
| **Purpose**      | File transfers between hosts                                                |
| **Authentication**| Username/password (plaintext) or anonymous access                           |
| **Security**     | FTPS adds SSL/TLS encryption                                                |
| **Port**         | 20 (data), 21 (control)                                                     |

---

## Transport Layer Protocols
### Key Responsibilities
- End-to-end communication channels
- Port-based process identification
- Reliability mechanisms (TCP only)

---

### TCP vs UDP Comparison
| Feature               | TCP                                      | UDP                                      |
|-----------------------|------------------------------------------|------------------------------------------|
| **Connection**        | Connection-oriented (3-way handshake)    | Connectionless                           |
| **Reliability**       | Guaranteed delivery (ACKs/retransmits)   | Best-effort delivery                     |
| **Speed**             | Slower (overhead)                        | Faster (minimal overhead)                |
| **Use Cases**         | Web, email, file transfers               | VoIP, video streaming, DNS               |

---

### TCP Key Mechanisms
1. **Three-Way Handshake**  
   Client → SYN → Server  
   Client ← SYN-ACK ← Server  
   Client → ACK → Server  

2. **Sequence/Acknowledgement Numbers**  
   - Track byte order (e.g., SEQ=0-9 → ACK=10)
   - Enable retransmission of lost segments

3. **Flow Control**  
   - Dynamic window sizing (receiver advertises buffer capacity)
   - Prevents sender overloading receiver

---

### Port Number System
| Port Range      | Usage                           | Examples                          |
|-----------------|---------------------------------|-----------------------------------|
| 0-1023          | Well-known services             | HTTP (80), FTP (21), SSH (22)     |
| 1024-49151      | Registered applications         | MySQL (3306), RDP (3389)          |
| 49152-65535     | Ephemeral (client-side)         | Dynamic client connections        |

---

## Internet Layer (IPv4)
### Address Structure
- **32-bit address**: 192.168.1.10 (dotted decimal)
- **Network/Host Parts**:  
  Network: 192.168.1.0  
  Host:    192.168.1.10  
  Subnet Mask: 255.255.255.0  

---

### Routing Fundamentals
| Concept          | Description                                                                 |
|------------------|-----------------------------------------------------------------------------|
| **Router**       | Forwards packets between networks using routing tables                      |
| **Hop-by-Hop**   | Each router makes independent forwarding decisions                          |
| **Routing Table**| Maps destination networks → next-hop interfaces                            |

---

## Data Flow Through Layers
Application Layer: HTTP Request → (Message)
Transport Layer:   Add TCP Header → (Segment)
Internet Layer:    Add IP Header → (Packet)
Network Access:    Add Frame Header → Transmit Bits

---

## Key Takeaways
1. **Application Layer** formats messages for specific services
2. **Transport Layer** manages end-to-end delivery (TCP/UDP)
3. **Internet Layer** handles addressing/routing (IPv4)
4. **Layered Design** enables modular network operations

---

> **Next Unit**: Ethernet networking - MAC addressing, switching, and physical layer considerations.
