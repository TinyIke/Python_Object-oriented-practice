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
        