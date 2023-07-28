import socket

BUFF_SIZE = 4096
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF,BUFF_SIZE)
host_name = socket.gethostname()
host_ip = '192.168.56.1'
print(host_ip)
port =9999
socket_addr = (host_ip,port)
print('Listrning at:',socket_addr)
server_socket.bind(socket_addr)




try:
    data, addr = server_socket.recvfrom(BUFF_SIZE)
    with open("received_image.png", 'wb') as file:
        file.write(data)
    print("Image received and saved as 'received_image.jpg'.")
except KeyboardInterrupt:
    print("\nUser interrupted. Closing the socket.")
finally:
    server_socket.close()
    



# msg, client_addr = server_socket.recvfrom(BUFF_SIZE)
# print("GOT connection from", client_addr)
# print(msg)