from flask import Flask, render_template, request
import socket

app = Flask(__name__)

def send_dns_req(domain):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect(('192.168.213.246', 6969))
        client_socket.send(domain.encode())
        response = client_socket.recv(1024).decode()
        return f"Response for {domain}: {response} (type A record)"

def add_new_domain(domain_name):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect(('192.168.213.246', 6969))
        client_socket.send(f"ADD_DOMAIN {domain_name}".encode())
        response = client_socket.recv(1024).decode()
        return f"Response for {domain_name}: {response} (type A record)"

def canonical_name(domain_name_alias):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect(('192.168.213.246', 6969))
        client_socket.send(f"CANONICAL_NAME {domain_name_alias}".encode())
        response = client_socket.recv(1024).decode()
        return f"Response for {domain_name_alias}: {response} (type CNAME record)"

def aliases_name(domain_name):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect(('192.168.213.246', 6969))
        client_socket.send(f"ALIAS {domain_name}".encode())
        response = client_socket.recv(1024).decode()
        return f"Response for {domain_name}: {response} (type CNAME record)"

def mail_alias(domain_name):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect(('192.168.213.246', 6969))
        client_socket.send(f"MAIL_ALIAS {domain_name}".encode())
        response = client_socket.recv(1024).decode()
        return f"Response for {domain_name}: {response} (type MX record)"

def mail_name(domain_name):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect(('192.168.213.246', 6969))
        client_socket.send(f"MAIL_NAME {domain_name}".encode())
        response = client_socket.recv(1024).decode()
        return f"Response for {domain_name}: {response} (type MX record)"


@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    if request.method == 'POST':
        prompt = request.form.get('prompt')
        action = request.form.get('action')
        
        if action == 'send_dns_req':
            result = [send_dns_req(prompt)]
        elif action == 'add_new_domain':
            result = [add_new_domain(prompt)]
        elif action == 'canonical_name':
            result = [canonical_name(prompt)]
        elif action == 'aliases_name':
            result = [aliases_name(prompt)]
        elif action == 'mail_alias':
            result= [mail_alias(prompt)]
        elif action == 'mail_name':
            result = [mail_name(prompt)]

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)