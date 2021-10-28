'''
此為客戶端內主程式，

'''


import Db_handler
import AddEmployee
import SearchEmployee
import DeleteEmployee
import get_all_employee

import client2


host = "127.0.0.1"
port = 20001
BUFFER_SIZE = 1940
client = client2.ConnectServer(host, port)
Data_Object = Db_handler.Db_handler(client)
Choise = {}
Choise[1] = AddEmployee.AddEmployee(Data_Object)
Choise[2] = get_all_employee.Get_all_employee(Data_Object)
Choise[3] = SearchEmployee.SearchEmployee(Data_Object)
Choise[4] = DeleteEmployee.DeleteEmployee(Data_Object)


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