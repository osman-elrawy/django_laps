from Classes.Person  import *

import re
class Employe(Person):
    Employes = []
    def __init__(self,id ,car,email,salary,name,money,healthRate):
        super(Employe,self).__init__(name,money,healthRate)
        self.id=id
        self.car=car
        self.__email=email
        self.__salary=salary
        self.Fname=name
        self.Employes.append((self.id, self.car,self.email ,self.salary, self.name,self.money, self.healthRate))





    @property
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self,newsalary):
        if(newsalary<=1000):
            print('cannt change ')
        else:
            self.__salary=newsalary


    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self,newemail):
        email_validate_pattern = r"^\S+@\S+\.\S+$"
        if( re.match(email_validate_pattern, "hello@uibakery.io")):
            self.__email = newemail
        else:
            print('cannt change ')


    def work(self,hours):
        if hours == 8:
            Person.mood = self.moods[0]
            return  Person.mood
        elif hours > 8:
            Person.mood = self.moods[1]
            return Person.mood
        elif hours < 8:
            Person.mood = self.moods[2]
            return Person.mood




    def drive(self,distance):
        last=distance/10
        self.car.fuelRate = self.car.fuelRate*last*10/100
        print(self.car.fuelRate)
    def refuel(self,amount):
        self.car.fuelRate+=amount
        print("Added Succesful" ,  self.car.fuelRate)
    def send_mail(self,to,subject,msg,receiver_name):
        @property
        def email(self):
            return self.__email

        @email.setter
        def email(self, newemail):
            email_validate_pattern = r"^\S+@\S+\.\S+$"
            if (re.match(email_validate_pattern, newemail)):
                self.__email = newemail
            else:
                print('cannt change ')
