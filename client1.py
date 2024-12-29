import socket

def send_dns_req(domain):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        print("Connecting..")
        client_socket.connect(('192.168.247.246',6969)) #10.113.16.148 mine
        print(f"Connected at 192.168.247.246 at port 6969")
        client_socket.send(domain.encode())
        response= client_socket.recv(1024).decode()
        print(f"Response for {domain} : {response}")

for i in range(2):
    send_dns_req('amazon.com')
    send_dns_req('bing.com')