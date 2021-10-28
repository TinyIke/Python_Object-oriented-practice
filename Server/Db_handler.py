import pickle
import Employee
        
class Db_handler():
    def __init__(self):
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
        if (target_ID in self.database.keys()):
            return True
        else:
            return False
    def add_modify_employee(self,name,id,type,num_a,num_b):
        if(type == 1):
            self.database[id] = Employee.WorkerClass(name,id,type,num_a,num_b)
        else:
            self.database[id] = Employee.SupervisorClass(name,id,type,num_a,num_b)
        self.save(self.database)
    def del_employee(self,id):
        if(self.Check_if_exist(id)):
            del self.database[id]
            self.save(self.database)
        else:
            print('ID not exist!')
    def look_up_employee(self,id):
        if(self.Check_if_exist(id)):
            print(self.database[id])
            return str(self.database[id])
        else:
            return 'ID not exist!'

    def list_all_employee(self):
        id_list = []
        for ID in self.database:
            id_list.append(ID)
        return id_list