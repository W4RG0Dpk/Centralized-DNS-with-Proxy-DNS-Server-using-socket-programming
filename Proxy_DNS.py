import socket
from threading import Thread
import sqlite3

main_dns_addr=('192.168.213.110',6969)

proxy_rotation_index={}

def query_proxy_dns_database(domain):
    conn= sqlite3.connect('proxy_dns.db')
    cursor= conn.cursor()
    cursor.execute("SELECT ip_addresses FROM proxy_records WHERE domain = ?", (domain,))
    result = cursor.fetchone()
    conn.close()
    return result[0].split(",") if result else None

def query_main_dns_server(domain):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as main_dns_socket:
            main_dns_socket.connect(main_dns_addr)
            main_dns_socket.send(domain.encode())
            response= main_dns_socket.recv(1024).decode()
            print(f"Main DNS server response for {domain}: {response}")
            if response.startswith("Domain"):
                print(response)
                _, ips = response.split(",")
                return ips
            else:
                return response
    except Exception as e:
        print(f"Failed to query main DNS server: {e}")
        return "ERROR: Unable to resolve domain"

def query_canonical_or_alias(domain):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as canonical_socket:
            canonical_socket.connect(main_dns_addr)
            canonical_socket.send(domain.encode())
            response= canonical_socket.recv(1024).decode()
            print(f"Main DNS server response for {domain}: {response}")
            return response
    except Exception as e:
        print("Failed to query main DNS server: ",e)
        return "ERROR: Unable to resolve request"

def query_mail(domain):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as mail_socket:
            mail_socket.connect(main_dns_addr)
            mail_socket.send(domain.encode())
            response= mail_socket.recv(1024).decode()
            print(f"Main DNS server response for {domain}: {response}")
            return response
    except Exception as e:
        print("Failed to query main DNS server: ",e)
        return "ERROR: Unable to resolve request"

def get_rotated_ip(ips, domain):
    if domain not in proxy_rotation_index:
        proxy_rotation_index[domain] =0

    ip=ips[proxy_rotation_index[domain]]
    proxy_rotation_index[domain]= (proxy_rotation_index[domain] +1) % len(ips)
    return ip

def handle_client(client_socket, addr):
    try:
        domain = client_socket.recv(1024).decode().strip()
        print(f"Proxy DNS received request for: {domain} from: {addr}")
        
        if domain.startswith("CANONICAL_NAME") or domain.startswith("ALIAS"):
            response = query_canonical_or_alias(domain)
        elif domain.startswith("MAIL_ALIAS") or domain.startswith("MAIL_NAME"):
            response=query_mail(domain)
        else:
            ips = query_proxy_dns_database(domain)
            if ips:
                response = get_rotated_ip(ips, domain)
                print(f"Proxy DNS resolved locally: {domain} -> {response} and response given to: {addr}")
            else:
                response = query_main_dns_server(domain)
                print(f"Proxy DNS resolved via Main DNS: {domain} -> {response} and response given to: {addr}")
        client_socket.send(response.encode())
    except Exception as e:
        print("An error occurred:", e)
    finally:
        client_socket.close()     

def start_proxy_dns_server():
    """Start the proxy DNS server."""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('192.168.213.110', 6969))  #ip, port no.
    server_socket.listen(5)
    print("Proxy DNS Server is running on port 6969...")
    while True:
        client_socket, addr = server_socket.accept()
        Thread(target=handle_client, args=(client_socket,addr)).start()

start_proxy_dns_server()