import socket
import selectors
import main
import client


def start(selector):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 5001))
    server_socket.listen()
    selector.register(fileobj=server_socket, events=selectors.EVENT_READ, data=accept_connection(server_socket, selector))

def accept_connection(server_socket, selector):
    client_socket, addr = server_socket.accept()
    print('Connection from', addr)
    response = 'Wellcome my Server\n'.encode()
    response  += '1.Add car\n2.List of car\n3.Remove car\n0.Exit\n'.encode()
    client_socket.send(response)
    selector.register(fileobj=client_socket, events=selectors.EVENT_READ, data=client.send_message)


def add_car(client_socket):
    request = client_socket.recv(4096)
    print(request.decode())
    if request:
        response = 'Hello world\n'.encode()
        client_socket.send(response)
    else:
        main.selector.unregister(client_socket)
        client_socket.close()