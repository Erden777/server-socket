import main

def send_message(client_socket):
    request = client_socket.recv(4096)
    print('Hello')
    print(request.decode())
    if request:
        response = 'Hello world\n'.encode()
        client_socket.send(response)
        
    else:
        main.selector.unregister(client_socket)
        client_socket.close()