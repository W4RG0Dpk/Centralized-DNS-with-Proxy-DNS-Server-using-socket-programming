# README for Centralized DNS with Proxy DNS Server

---

## 🌐 **Project Title:** Centralized DNS with Proxy DNS Server

**A comprehensive system demonstrating how DNS works behind the scenes, implementing load distribution, hostname aliasing, and mail aliasing.**

---

## 🎨 **Overview**

This project emulates the real-world DNS resolution process by integrating a **Centralized DNS** with a **Proxy DNS Server**, using **socket programming**. It simplifies the complex layers of DNS lookup for end-users, showcasing an abstraction of what happens when they enter a URL in their browser.

Key features include:

- **Proxy DNS Server:** Acts as a low-level local DNS server for faster response times.
- **Centralized DNS:** Resolves requests forwarded by the proxy server when not available locally.
- **Load Distribution:** Efficient IP rotation for scalability and performance.
- **Hostname Aliasing:** Simplifies URLs with canonical name records (CNAME).
- **Mail Aliasing:** Supports mail server lookups with MX records.
- **Domain Addition:** Clients can add new domains dynamically.

---

## 🔗 **System Architecture**

The project is divided into:

1. **Client Application:** A Flask-based web interface to send DNS requests and interact with the server.
2. **Proxy DNS Server:** Handles local requests and forwards unresolved queries to the main DNS server.
3. **Main DNS Server:** Manages a centralized database for DNS resolution.
4. **Database Management:** SQLite databases for main DNS, proxy DNS, canonical records, and mail aliases.

---

## 🌐 **How It Works**

1. **Client Interaction:**\
   The client sends a query (e.g., domain lookup) via the web interface.
2. **Proxy Resolution:**\
   The proxy DNS attempts to resolve the query locally.
3. **Fallback to Main DNS:**\
   If unresolved, the proxy forwards the query to the main DNS.
4. **Database Lookup:**\
   The main DNS fetches data from its database or adds new entries as needed.
5. **Response to Client:**\
   Resolved IPs, aliases, or error messages are returned to the client.

---

## 🎡 **Features in Detail**

### **1. Load Distribution**

- Ensures fair distribution of traffic across multiple IPs for the same domain.
- Implemented via round-robin rotation.

### **2. Hostname Aliasing**

- Maps multiple aliases to canonical names, e.g., `yt.in -> youtube.com`.

### **3. Mail Aliasing**

- Handles mail server lookups using MX records.

### **4. Dynamic Domain Addition**

- Allows clients to register new domains with auto-generated IPs.

### **5. Proxy Optimization**

- Local caching in the proxy for faster lookups and reduced main DNS load.

---

## 📚 **Code Structure**

- `` Web client using Flask for user interactions.
- `` Proxy DNS server handling local lookups and main DNS forwarding.
- `` Centralized DNS server with load distribution and aliasing.
- `` Initializes databases with predefined records.

---

## 🚀 **How to Run**

### **Step 1:** Set Up Databases

Run `add_records.py` to create and populate the SQLite databases:

```bash
python add_records.py
```

### **Step 2:** Start Servers

1. Start the Main DNS Server:
   ```bash
   python main_DNS.py
   ```
2. Start the Proxy DNS Server:
   ```bash
   python Proxy_DNS.py
   ```

### **Step 3:** Start the Client Application

Launch the Flask web app:

```bash
python client.py
```

Access the web interface at `http://127.0.0.1:5000`.

---

## 📷 **Screenshots**

### **Client Web Interface**

### **DNS Resolution Output**

---

## 🔄 **Future Enhancements**

- Add support for IPv6 records.
- Implement advanced caching techniques for the proxy server.
- Introduce HTTPS for secure communications.

---



Feel free to contribute to this project and make DNS resolution even more fascinating!

**Contact:** For queries, reach out at [velamalapavankrishna@gmail.com](mailto\:velamalapavankrishna@gmail.com).
OR
you can reach me out at insta : pavankrishna_v

