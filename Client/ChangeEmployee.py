class ChangeEmployee():
    def __init__(self,Data_Object):
        self.Data = Data_Object
        self.database = Data_Object.database
    def execute(self):
        id = input('Please enter the employee ID:')
        if(self.Data.Check_if_exist(id)):
            name = input('Current name is {}, enter a new name:'.format(self.database[id].Name))
            if(self.database[id].Employee_type == 1):
                shift = input('Current shift is {}, new shift:'.format(self.database[id].Shift))
                rate = input('Current rate is {}, new rate:'.format(self.database[id].Rate))
                self.Data.add_modify_employee(name,id,self.database[id].Employee_type,shift,rate)
            else:
                salary = input('Current salary is {}, new salary:'.format(self.database[id].Salary))
                bonus = input('Current bonus is {}, new bonus:'.format(self.database[id].Bonus))
                self.Data.add_modify_employee(name,id,self.database[id].Employee_type,salary,bonus)
        else:
            print('Loop up fail! No such employee!')