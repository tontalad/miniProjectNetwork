import socket

BUFF_SIZE = 4096
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.setsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF,BUFF_SIZE)
host_name = socket.gethostname()
host_ip =  socket.gethostbyname(host_name)  #'192.168.1.10'
port = 9999
message = b"Hello World"
print(host_ip)
image_path = 'image/image1.png'
with open(image_path, 'rb') as file:
    image_data = file.read()

# Send the image data over the UDP socket
client_socket.sendto(image_data,(host_ip,port))

print("Image sent successfully.")