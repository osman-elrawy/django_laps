from Classes.Employe import *
class Office:
    def __init__(self,name,employees):
        self.name=name
        self.employees=employees
    def get_all_employees(self):
        print(Employe.Employes)

    def get_employee(self,name):
        data=Employe.Employes
        for index,item in enumerate(data):
            for i in item:
                if i==name:
                    return Employe.Employes[index]


    def hire(self):
        print("hire EMPLOYE")
    def fire(self,name):
        data=Employe.Employes
        for index,item in enumerate(data):

             for index2,i in enumerate(item):
                    if i==name:
                     Employe.Employes.pop(index)
    def check_lateness(self):
        print("calculate_lateness")

    def calculate_lateness(self):
        print("calculate_lateness")
    def deduct(self,empId,deduction):
        data=Employe.Employes
        for index,item in enumerate(data):
             Listt=list(item)
             for index2,i in enumerate(item):
                    if i==empId:
                     Employe.Employes.pop(index)
                     Listt[index2+3]-=Listt[index2+3]*(deduction/100)
                     final=tuple(Listt)
                     Employe.Employes.append(final)
             break


    def reward(self,empId,reward):
        data=Employe.Employes
        for index,item in enumerate(data):
             Listt=list(item)
             for index2,i in enumerate(item):
                    if i==empId:
                     Employe.Employes.pop(index)
                     Listt[index2+3]+=Listt[index2+3]*reward/100
                     Employe.Employes.append(tuple(Listt))
             break

