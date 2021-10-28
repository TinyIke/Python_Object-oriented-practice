import socket
from threading import Thread
import json



host = "127.0.0.1"
port = 20001


class PureSocketServer(Thread):
    def __init__(self, host, port, Data_Object):
        super().__init__()
        self.__server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__server_socket.bind((host, port))
        self.__server_socket.listen(5)
        
        self.Data_Object = Data_Object


    def serve(self):
        self.start()

    def run(self):
        while True:
            connection, address = self.__server_socket.accept()
            print("{} connected".format(address))
            self.new_connection(connection=connection,
                                                  address=address)

    def new_connection(self, connection, address):
        Thread(target=self.receive_message_from_client,
               kwargs={
                   "connection": connection,
                   "address": address}, daemon=True).start()

    def receive_message_from_client(self, connection, address):
        keep_going = True
        while keep_going:
            try:
                message = connection.recv(1024).strip().decode()
            except:
                keep_going = False
            else:
                if not message:
                    break
                message = json.loads(message)
                
                if message['command'] == "close":
                    connection.send("closing".encode())
                    break
                elif message['command'] == 'check_if_exist':
                    exist_flag = self.Data_Object.Check_if_exist(message['parameter']['employee_id'])
                    #print (exist_flag)
                    reply_msg = {"status": "OK", "parameter": {"exist_flag": exist_flag}}
                    connection.send(json.dumps(reply_msg).encode())
                    
                elif message['command'] == 'add_modify_employ':
                    name = message['parameter']['name']
                    id = message['parameter']['employee_id']
                    shift = message['parameter']['shift']
                    rate = message['parameter']['rate']
                    salary = message['parameter']['salary']
                    bonus = message['parameter']['bonus']
                    if message['parameter']['employee_type'] == 'worker':
                        self.Data_Object.add_modify_employee(name, id, 1, shift, rate)
                    else:
                        self.Data_Object.add_modify_employee(name, id, 2, salary, bonus)
                    reply_msg = {"status": "OK", "parameter": -1}
                    connection.send(json.dumps(reply_msg).encode())

                elif message['command'] == 'list_all_employee':
                    id_list = self.Data_Object.list_all_employee()
                    reply_msg = {"status": "OK", "parameter": {"employ_list": id_list}}
                    connection.send(json.dumps(reply_msg).encode())

                elif message['command'] == 'look_up_employee':
                    id = message['parameter']['employee_id']
                    information = self.Data_Object.look_up_employee(id)
                    reply_msg = {"status": "OK", "parameter": {"information": information}}
                    connection.send(json.dumps(str(reply_msg)).encode())
                
                elif message['command'] == 'del_employ':
                    id = message['parameter']['employee_id']
                    self.Data_Object.del_employee(id)
                    reply_msg = {"status": "OK", "parameter": -1}
                    connection.send(json.dumps(reply_msg).encode())
                
                else:
                    print(message)
                    reply_msg = "receive {}".format(message['command'])
                    connection.send(json.dumps(reply_msg).encode())
                
                
        
        print("close connection")
        

if __name__ == '__main__':
    server = PureSocketServer(host, port)
    server.serve()
