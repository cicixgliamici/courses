# Internet Fundamentals: Core Concepts & Extended Insights  

## DNS Caching & Optimization  
### How DNS Resolution Works  
When you visit a domain (e.g., `example.com`), your device first checks its **local DNS cache**—a temporary storage for recently resolved domain-to-IP mappings. If unavailable, a recursive query is sent to DNS servers.  

**Key Enhancements**:  
- **TTL (Time to Live)**: Administrators set TTL values (e.g., 3600 seconds) to control how long records stay cached. Lower TTLs allow faster updates but increase DNS queries.  
- **DNS Record Types**: Beyond A (IPv4) and AAAA (IPv6), `CNAME` aliases (e.g., `www.example.com` → `example.com`) streamline domain management.  
- **Global CDNs**: Services like Cloudflare use geographically distributed caches to reduce latency.  

> **Example**: After closing/reopening `example.com`, the browser skips DNS lookups if the cached IP hasn’t expired.  

---

## TCP/IP: The Backbone of Internet Communication  
### Packet-Switched Networking  
TCP/IP breaks data into **packets** with headers containing source/destination IPs and sequencing info. Unlike UDP (connectionless), TCP guarantees delivery via:  
1. **Three-Way Handshake**: `SYN` → `SYN-ACK` → `ACK` to establish connections.  
2. **Error Correction**: Retransmits lost packets.  
3. **OSI Layers**: Operates at **Transport (TCP)** and **Network (IP)** layers.  

**Extended Use Cases**:  
- **IoT Devices**: Often use UDP for real-time data (e.g., sensors) due to lower overhead.  
- **VPNs**: Encapsulate TCP/IP packets within secure tunnels.  

---

## HTTP/HTTPS & Secure Communication  
### Protocol Evolution  
| Feature          | HTTP                              | HTTPS                             |  
|------------------|-----------------------------------|-----------------------------------|  
| **Security**     | Unencrypted                       | Encrypted (SSL/TLS)               |  
| **Port**         | 80                                | 443                               |  
| **Use Case**     | Static content                    | Login pages, e-commerce           |  

**SSL/TLS Handshake Simplified**:  
1. Client requests HTTPS connection.  
2. Server sends certificate (with public key).  
3. Client validates certificate (e.g., via Certificate Authorities like Let’s Encrypt).  
4. Session key exchange enables encrypted communication.  

**Advanced Concepts**:  
- **HSTS**: Forces browsers to use HTTPS via `Strict-Transport-Security` header.  
- **HTTP/2**: Multiplexes requests over a single connection for faster loading.  

---

## HTTP Methods & Headers  
### Common Methods  
| Method   | Purpose                                  | Example                          |  
|----------|------------------------------------------|----------------------------------|  
| `GET`    | Retrieve data                            | Loading a webpage                |  
| `POST`   | Submit data                              | Form submissions                 |  
| `PUT`    | Update/replace resource                  | Editing user profiles            |  
| `DELETE` | Remove resource                          | Deleting a file                  |  
| `PATCH`  | Partial updates                          | Modifying a settings field       |  

**Headers in Action**:  
- `User-Agent`: Identifies client software (e.g., Chrome, iOS).  
- `Cache-Control`: Directs caching behavior (e.g., `max-age=86400`).  

---

## Network Ports & Firewalls  
### Well-Known Ports  
| Port  | Service          | Description                          |  
|-------|------------------|--------------------------------------|  
| 22    | SSH              | Secure remote server access          |  
| 53    | DNS              | Domain name resolution               |  
| 80    | HTTP             | Unencrypted web traffic              |  
| 443   | HTTPS            | Encrypted web traffic                |  
| 3306  | MySQL            | Database connections                 |  

**Firewall Strategies**:  
- **Whitelisting**: Allow traffic only on specific ports (e.g., 443 for web apps).  
- **Stateful Inspection**: Tracks active connections to block unsolicited traffic.  

**Ephemeral Ports** (49152–65535): Used temporarily by clients for outbound requests.  

---

## Best Practices for Security & Performance  
1. **Minimize Open Ports**: Close unused ports to reduce attack surfaces.  
2. **Enable TLS 1.3**: Offers faster, more secure encryption than older versions.  
3. **Monitor DNS Cache**: Use `ipconfig /flushdns` (Windows) or `sudo systemd-resolve --flush-caches` (Linux) to troubleshoot stale records.  
4. **Leverage CDNs**: Cache static assets globally to reduce latency.  
