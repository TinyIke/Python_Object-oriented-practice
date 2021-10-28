class DeleteEmployee():
    def __init__(self,Data_Object):
        self.Data = Data_Object
        self.database = Data_Object.database
    def execute(self):
        id = input('Please enter the employee ID:')
        self.Data.del_employee(id)