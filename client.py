from socket import *
IP = gethostbyname(gethostname())
PORT = 5555
DISCONNECT = "Client Dropped"
ADDR = (IP,PORT)
s = socket(AF_INET,SOCK_STREAM)
s.connect(ADDR)
connected = True
while connected:    
  data = raw_input("Msg ---> ")    
  data = data.encode("utf-8")   
  if data.decode("utf-8") == "exit":         
    s.send("Client Dropped".encode("utf-8"))          
    connected = False   
  s.send(data)
print("Disconnected successfully !")
s.close()
