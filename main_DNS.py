import socket 
import sqlite3
from threading import Thread
import random
import string
mainDNS=r"C:\amrita_uni\s3\Computer Networks\DNS resolver\main_dns.db"
canonical=r"C:\amrita_uni\s3\Computer Networks\DNS resolver\canonical.db"
mail_alias=r"C:\amrita_uni\s3\Computer Networks\DNS resolver\mail_alias.db"

rotation_index={}

def query_main_dns_database(domain_name):
    conn= sqlite3.connect(mainDNS)
    cursor= conn.cursor()
    cursor.execute("SELECT ip_addresses FROM dns_records WHERE domain = ?", (domain_name,))
    result= cursor.fetchone()
    conn.close()
    return result[0].split(",") if result else None

def generate_alias(domain_name):
    alias_prefix = ''.join(random.choices(string.ascii_lowercase, k=3))
    alias_name = f"{alias_prefix}.{domain_name}"
    return alias_name

def add_alias_to_canonical(domain_name):
    conn= sqlite3.connect(canonical)
    cursor= conn.cursor()
    #check in canonical.db
    cursor.execute("SELECT aliases FROM canonical_records WHERE canonical_name = ?", (domain_name,))
    result = cursor.fetchone()
    if result :
        existing_aliases = result[0].split(',')
        new_alias = generate_alias(domain_name)

        if new_alias not in existing_aliases:
            existing_aliases.append(new_alias)
            updated_aliases = ','.join(existing_aliases)

            cursor.execute(
                "UPDATE canonical_records SET aliases = ? WHERE canonical_name = ?",
                (updated_aliases, domain_name)
            )
            conn.commit()
            print(f"Added new alias {new_alias} for domain {domain_name}.")
        else:
            print(f"Alias {new_alias} already exists for domain {domain_name}.")
    else:
        # If the canonical domain does not exist, add it with the new alias
        new_alias = generate_alias(domain_name)
        cursor.execute(
            "INSERT INTO canonical_records (canonical_name, aliases) VALUES (?, ?)",
            (domain_name, new_alias)
        )
        conn.commit()
        print(f"Added domain {domain_name} with alias {new_alias} to canonical records.")

    conn.close()

def get_rotated_ip(ips, domain):
    if domain not in rotation_index:
        rotation_index[domain]=0
    ip= ips[rotation_index[domain]]
    rotation_index[domain]= (rotation_index[domain] +1) % len(ips)

    return ip

def handle_client(client_socket,addr):
    try:
        domain = client_socket.recv(1024).decode().strip()
        print(f"Main DNS received request for: {domain} from : {addr}")
        if domain.startswith("ADD_DOMAIN"):
            _ , domain_name= domain.split(maxsplit=1)
            ips= add_domain_to_database(domain_name)
            if ips:
                add_alias_to_canonical(domain_name)
                print(f"Domain {domain_name} added with IPs: {', '.join(ips)}")
                client_socket.send(get_rotated_ip(ips,domain).encode())
            else:
                response= f"Domain {domain_name} already exists."
                print(response)
                client_socket.send(response.encode())
        elif domain.startswith("CANONICAL_NAME") or domain.startswith("ALIAS"):
            handle_canonical_query(client_socket,addr,domain)
        elif domain.startswith("MAIL_ALIAS") or domain.startswith("MAIL_NAME"):
            handle_mail_alias(client_socket, addr, domain)
        else:
            ips= query_main_dns_database(domain)

            if ips:
                ip= get_rotated_ip(ips,domain)
                print(f"Main DNS resolved: {domain} -> {ip} from  : {addr}")
            else:
                ip= "Domain not found."
            client_socket.send(ip.encode())    
    finally:
        client_socket.close()

def generate_random_ips(num=3):
    return [f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}" for _ in range(num)]

def add_domain_to_database(domain_name):
    ip_addresses = generate_random_ips()
    conn = sqlite3.connect(mainDNS)  
    cursor = conn.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS dns_records (
        domain TEXT PRIMARY KEY,
        ip_addresses TEXT
    )
    """)
    
    cursor.execute("SELECT ip_addresses FROM dns_records WHERE domain = ?", (domain_name,))
    result = cursor.fetchone()
    if result:
        conn.close()
        print(f"Domain {domain_name} already exists with IPs: {result[0]}")
        return None
    
    cursor.execute(
        "INSERT OR REPLACE INTO dns_records (domain, ip_addresses) VALUES (?, ?)",
        (domain_name, ','.join(ip_addresses))
    )
    conn.commit()
    conn.close()
    print(f"Added domain: {domain_name} with IPs: {', '.join(ip_addresses)}")
    return ip_addresses


def handle_canonical_query(client_socket, addr, domain):
    conn= sqlite3.connect(canonical)
    cursor = conn.cursor()
    print(f"Main DNS received request for: {domain} from : {addr}")
    response="Not found"
    try:
        if domain.startswith("CANONICAL_NAME"): # to check given alias and get canonical
            _, alias_name= domain.split(maxsplit=1)
            cursor.execute("SELECT canonical_name FROM canonical_records WHERE aliases LIKE ?", 
               (f"%{alias_name}%",))
            result = cursor.fetchone()
            if result:
                response= result[0]
        elif domain.startswith("ALIAS"):  #to check given canonnical and get alias
            _, canonical_name = domain.split(maxsplit=1)
            cursor.execute("SELECT aliases FROM canonical_records WHERE canonical_name = ?", 
                (canonical_name,))
            result = cursor.fetchone()
            if result:
                response = result[0]
        else:
            response= "Invalid Request"
    except Exception as e:
        response= f"Error: {e}"
    finally:
        print(f"MAIN DNS Resolved {domain} : {response}")
        conn.close()
        client_socket.send(response.encode())

def handle_mail_alias(client_sock, addr, domain):
    conn= sqlite3.connect(mail_alias)
    cursor= conn.cursor()
    print(f"Main DNS received request for: {domain} from : {addr}")
    response="Not found"
    try:
        if domain.startswith("MAIL_NAME"): # to check alias and get canonical
            _, alias_name= domain.split(maxsplit=1)
            cursor.execute("SELECT email FROM mail_alias_records WHERE aliases LIKE ?", 
               (f"%{alias_name}%",))

            result = cursor.fetchone()
            if result:
                response= result[0]
        elif domain.startswith("MAIL_ALIAS"): #to check canonical and get aliases
            _, canonical_name = domain.split(maxsplit=1)
            cursor.execute("""
    SELECT aliases FROM mail_alias_records 
    WHERE email = ?
""", (canonical_name,))

            result = cursor.fetchone()
            if result:
                response = result[0]
        else:
           response="Invalid response"
    except Exception as e:
        response= f"Error : {e}"
    finally:
        print(f"MAIN DNS Resolved {domain} : {response}")
        conn.close()
        client_sock.send(response.encode())

def start_main_dns():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    server_socket.bind(('192.168.213.110',6969)) #ip , port
    server_socket .listen(5) #at max 5 connections
    print("Main DNS Server is running on port 6969...\n")
    while True:
        client_socket, addr = server_socket.accept()
        Thread(target=handle_client, args=(client_socket,addr)).start()  #new thread will use func handle_client with args as tuple given

start_main_dns()
