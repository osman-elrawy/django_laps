
from  Classes.Employe import *


class Person:
    moods=('Happy','Lazy','Tired')
    def __init__(self,name,money,healthRate):
        self.name = name
        self.money = money

        self.healthRate = healthRate

    def sleep(self,hours):
        if hours ==7 :
            self.mood= self.moods[0]
        elif hours <7 :
            self.mood= self.moods[1]
        elif hours >7 :
            self.mood = self.moods[2]

        return print(self.name,"is",self.mood)
    def eat(self,meals):
        if meals ==3 :
            self.healthRate="100 HTH%"
        elif meals <7 :
            self.healthRate = "75% HTH "
        elif meals >7 :
            self.healthRate = "50% HTH"
    def buy(self,items ):

        self.money=self.money - 5*10/100


