class Get_all_employee():
    def __init__(self,Data_Object):
        self.Data = Data_Object
        self.database = Data_Object.database
    def execute(self):
        self.Data.list_all_employee()