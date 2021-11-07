class EmployeeClass():
    def __init__(self,name,id,type):
        self.Name=name
        self.ID=id
        self.Employee_type=type
        

class WorkerClass(EmployeeClass):
    def __init__(self,name,id,type,shift,rate):
        super().__init__(name,id,type)
        self.Shift=shift
        self.Rate=rate
    def __str__(self):
        return "W-Name:{},ID={},Shift={},Rate={}".format(self.Name,self.ID,self.Shift,self.Rate)

class SupervisorClass(EmployeeClass):
    def __init__(self,name,id,type,salary,bonus):
        super().__init__(name,id,type)
        self.Salary=salary
        self.Bonus=bonus
    def __str__(self):
        return "S-Name:{},ID={},Salary={},Bonus={}".format(self.Name,self.ID,self.Salary,self.Bonus)
