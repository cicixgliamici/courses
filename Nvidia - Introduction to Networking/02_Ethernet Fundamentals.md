# Ethernet Fundamentals

## Overview of Ethernet Technology
- **OSI Layers**: Operates at **Data Link Layer (L2)** and **Physical Layer (L1)**  
  - **Data Link Layer**: Manages node-to-node data transfer & error detection  
  - **Physical Layer**: Defines electrical/optical properties & transmission speeds  
- **Key Evolution**:  
  - 1970s: Invented by Robert Metcalfe (Xerox PARC)  
  - 1980s: Standardized as **IEEE 802.3**  
  - Speeds: 10 Mbps → 100 Mbps → 400 Gbps  

---

## MAC Addresses
### Structure & Assignment
- **48-bit address** (12 hex digits):  
  ```plaintext
  OUI (Vendor ID): First 6 digits (e.g., 00:1A:2B)  
  Serial Number: Last 6 digits (e.g., 3C:4D:5E)  
  ```
- **Uniqueness**: Burned into NIC hardware by vendors (IEEE-regulated OUIs)  

### Commands to View MAC Addresses
| OS       | Command     | Output Example            |
|----------|-------------|---------------------------|
| Linux    | `ifconfig`  | `ether 00:1a:2b:3c:4d:5e` |
| Windows  | `ipconfig`  | `Physical Address: 00-1A-2B-3C-4D-5E` |

---

## Ethernet Frame Structure
| Field               | Size (Bytes) | Description                              |
|---------------------|--------------|------------------------------------------|
| **Destination MAC** | 6            | Recipient’s MAC address                  |
| **Source MAC**      | 6            | Sender’s MAC address                     |
| **EtherType**       | 2            | Upper-layer protocol (e.g., IPv4=0x0800) |
| **Payload**         | 46-1500      | Data (MTU = 1500 bytes standard)         |
| **FCS (Trailer)**   | 4            | Error detection (CRC checksum)           |

- **Frame Size**: 64–1,518 bytes (excluding preamble)  
- **Jumbo Frames**: Non-standard payloads >1,500 bytes (vendor-specific)  

---

## Ethernet Switching & MAC Address Tables
### Switch Operations
1. **Learning**: Records source MAC → ingress port in **MAC Table**  
2. **Forwarding**: Uses destination MAC → egress port mappings  
3. **Aging**: Dynamic entries expire after 300s (default)  
4. **Flooding**: For unknown unicast/broadcast/multicast frames  

### Frame Types & Handling
| Frame Type          | MAC Address Format       | Switch Action            |
|---------------------|--------------------------|--------------------------|
| **Unicast**         | Specific destination     | Forward to mapped port   |
| **Unknown Unicast** | No MAC table entry       | Flood to all ports       |
| **Broadcast**       | `FF:FF:FF:FF:FF:FF`      | Flood to all ports       |
| **Multicast**       | First byte LSB=1 (e.g., `01:00:5E:xx:xx:xx`) | Flood (traditional switches) |

---

## Layer 2 vs Layer 3 Networking
| Feature              | Layer 2 Switch           | Layer 3 Switch (Multilayer) |
|----------------------|--------------------------|-----------------------------|
| **Forwarding Basis** | MAC addresses            | IP addresses                |
| **Functionality**    | Basic frame switching    | Routing + switching         |
| **Use Case**         | LAN segmentation         | Inter-VLAN routing          |

---

## Key Takeaways
1. **MAC Addresses** uniquely identify devices at L2.  
2. **Ethernet Frames** include headers for addressing and error checking.  
3. **Switches** use MAC tables to optimize frame forwarding.  
4. **Layer 3 Switches** combine routing and switching for flexible networks.  

---

> **Next Unit**: VLANs and advanced network segmentation strategies.  
