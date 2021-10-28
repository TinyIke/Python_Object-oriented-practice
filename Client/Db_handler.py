import pickle
import Employee
import json
        
class Db_handler():
    def __init__(self, client):
        self.client = client
        try:
            file = open('pickle_example.dat', 'rb')
            self.database = pickle.load(file)
            file.close()
        except:
            self.database = {}
        
    def save(self,database):
        try:
            file = open('pickle_example.dat', 'wb')
            pickle.dump(database, file)
            file.close()
        except:
            print('Error within saving!!')
        

    
            
    def Check_if_exist(self,target_ID):
        self.client.send_command('check_if_exist', {'employee_id': target_ID})
        self.client.wait_response()
        #print(self.client.reply_msg)
        return self.client.reply_msg['parameter']['exist_flag']

    def add_modify_employee(self,name,id,type,num_a,num_b):
        if(type == 1):
            self.client.send_command('add_modify_employ', 
                                     {'employee_type': 'worker',
                                      'name': name,
                                      'employee_id': id,
                                      'shift': num_a,
                                      'rate': num_b,
                                      'salary': 0,
                                      'bonus': 0})
        else:
            self.client.send_command('add_modify_employ', 
                                     {'employee_type': 'supervisor',
                                      'name': name,
                                      'employee_id': id,
                                      'shift': 0,
                                      'rate': 0,
                                      'salary': num_a,
                                      'bonus': num_b})
        self.client.wait_response()
    def del_employee(self,id):
        if(self.Check_if_exist(id)):
            self.client.send_command('del_employ', {'employee_id': id})
            self.client.wait_response()
        else:
            print('ID not exist!')
    def look_up_employee(self,id):
        if(self.Check_if_exist(id)):
            self.client.send_command('look_up_employee', {'employee_id': id})
            self.client.wait_response()
            self.reply_msg = "{}".format(self.client.reply_msg['parameter']['information'])
            print(self.reply_msg)
        else:
            print('ID not exist!')
    def list_all_employee(self):
        self.client.send_command('list_all_employee',{})
        self.client.wait_response()
        for id in self.client.reply_msg['parameter']['employ_list']:
            self.look_up_employee(id)