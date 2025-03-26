# Introduction to Networking Course

## Course Overview
This course introduces foundational concepts of computer networking. Key topics include:
- Network definitions and components
- Performance requirements in modern environments
- The OSI model and TCP/IP protocol suite
- Data encapsulation and transmission

---

## What is a Network?
A **network** is a system of interconnected nodes (devices) that exchange data such as:
- Voice/video streams  
- Storage resources  
- Management information  

---

## Network Requirements in High-Demand Environments
Modern applications (e.g., data center workloads) require networks to provide:
| Requirement       | Description                                                                 |
|-------------------|-----------------------------------------------------------------------------|
| **High Bandwidth** | Support large data transfers (e.g., video streaming, big data analytics)    |
| **Low Latency**    | Minimize delays for real-time applications (e.g., VoIP, online gaming)      |
| **High Availability** | Ensure 24/7 uptime through redundancy and failover mechanisms            |
| **Scalability**    | Adapt to growing traffic demands without major redesigns                   |

---

## Network Components
### End Nodes
- **Compute Nodes**: Servers/workstations generating/consuming data  
- **Storage Nodes**: Devices providing shared storage resources  
- **Management Nodes**: Systems controlling network operations  

### Intermediate Nodes
- **Switches**: Forward traffic within local networks (Layer 2)  
- **Routers**: Direct traffic between different networks (Layer 3)  

---

## Building a Simple Network
1. **NIC Installation**: Each end node requires a Network Interface Card (NIC) with physical ports.
2. **Cabling**: Connect NIC ports to switch ports via Ethernet cables.
3. **Protocol Configuration**: Implement compatible communication protocols on all devices.

---

## Communication Protocols & Protocol Suites
- A **protocol** defines rules for:  
  - Session establishment/termination  
  - Message formatting  
  - Error handling  
- A **protocol suite** combines multiple protocols for end-to-end communication (e.g., TCP/IP).

---

## The OSI Model
A 7-layer framework standardizing network communication:

| Layer  | Name               | Functionality Example                     |
|--------|--------------------|-------------------------------------------|
| 7      | Application        | HTTP, FTP                                 |
| 6      | Presentation       | Data encryption/compression               |
| 5      | Session            | Connection setup/teardown                 |
| 4      | Transport          | TCP/UDP segmentation                      |
| 3      | Network            | IP addressing/routing                     |
| 2      | Data Link          | MAC addressing, switching                 |
| 1      | Physical           | Cabling, bit transmission                 |

**Advantages of Layering**:  
- Simplifies troubleshooting  
- Enables modular technology development  
- Standardizes vendor interoperability  

---

## TCP/IP Protocol Suite
Developed for ARPANET (predecessor to the Internet), this 4-layer model combines OSI functionalities:

| TCP/IP Layer      | Equivalent OSI Layers     | Key Protocols          |
|-------------------|---------------------------|------------------------|
| Application       | 5+6+7                     | HTTP, FTP, DNS         |
| Transport         | 4                         | TCP, UDP               |
| Internet          | 3                         | IPv4, IPv6             |
| Network Access    | 1+2                       | Ethernet, Wi-Fi        |

---

## Data Encapsulation Process
Data undergoes transformations as it traverses network layers:

1. **Application Layer**: Generates raw data (message)
2. **Transport Layer**: Adds port numbers → creates *segment* (TCP) or *datagram* (UDP)
3. **Internet Layer**: Adds IP addresses → creates *packet*
4. **Data Link Layer**: Adds MAC addresses → creates *frame*
5. **Physical Layer**: Converts to bits for transmission

---

## Key Networking Devices by Layer
| Layer  | Device       | Functionality                          |
|--------|--------------|----------------------------------------|
| 3      | Router       | Routes packets between networks        |
| 2      | Switch       | Forwards frames within a network       |
| 1      | Hub/Repeater | Extends physical signal (obsolete)     |
