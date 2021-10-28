# Python TCP Client A
import socket 
import sys
import json

host = "127.0.0.1"
port = 20001
BUFFER_SIZE = 1940


class ConnectServer():
    def __init__(self, host, port):
        self.__client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        self.__client_socket.connect((host, port))
 
    def send_command(self, command, parameter):
        send_data = {'command': command, 'parameter': parameter}
        self.__client_socket.send(json.dumps(send_data).encode("utf-8"))

    def wait_response(self):
        data = self.__client_socket.recv(BUFFER_SIZE)
        raw_data = data.decode("utf-8")
        self.reply_msg = json.loads(raw_data)
        #print(raw_data)
        
        
        if raw_data == "closing":
            return False
        
        return True

    