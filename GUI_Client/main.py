'''
此為客戶端內主程式，

'''

import client2
import Db_handler
class AddEmployee():
    def __init__(self,Data_Object):
        self.Data = Data_Object
        self.database = Data_Object.database
        
    def execute(self):
        id = input('Please enter the employee ID:')
        if(self.Data.Check_if_exist(id)):
            print('ID already exist!')
        else:
            name = input('The employee name:')
            type = int(input('Type (1)Worker (2)Supervisor:'))
            if(type == 1):
                shift = input('Shift (1) day (2) night:')
                rate = input('Rate:')
                self.Data.add_modify_employee(name,id,type,shift,rate)
            else:
                salary = input('salary:')
                bonus = input('bonus:')
                self.Data.add_modify_employee(name,id,type,salary,bonus)
        
class SearchEmployee():
    def __init__(self,Data_Object):
        self.Data = Data_Object
        self.database = Data_Object.database
    def execute(self):
        id = input('Please enter the employee_id:')
        self.Data.look_up_employee(id)

class DeleteEmployee():
    def __init__(self,Data_Object):
        self.Data = Data_Object
        self.database = Data_Object.database
    def execute(self):
        id = input('Please enter the employee ID:')
        self.Data.del_employee(id)
        
class Get_all_employee():
    def __init__(self,Data_Object):
        self.Data = Data_Object
        self.database = Data_Object.database
    def execute(self):
        self.Data.list_all_employee()




host = "127.0.0.1"
port = 20001
BUFFER_SIZE = 1940
client = client2.ConnectServer(host, port)
Data_Object = Db_handler.Db_handler(client)
Choise = {}
Choise[1] = AddEmployee(Data_Object)
Choise[2] = Get_all_employee(Data_Object)
Choise[3] = SearchEmployee(Data_Object)
Choise[4] = DeleteEmployee(Data_Object)


while(True):
    
    
    print('---------Menu---------')
    print('1. Add a new employee')
    print('2. List all')
    print('3. Look up a employee')
    print('4. Delete a employee')
    print('0. Quit the program')
    choise = int(input('Enter your choise:'))
    if (choise == 0):
        print('bye')
        break
    else:
        Choise[choise].execute()
    #Data.save(Dict)