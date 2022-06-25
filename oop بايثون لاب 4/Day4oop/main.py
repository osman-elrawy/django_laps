
from  Classes.Employe import *
from  Classes.Car import *
from  Classes.Office import *
car1=Car("Fiat",100,20)
per1=Employe(70,car1,'SHAWKE1234%@yahoo.comsss',5000,'MAHMOUD AHMED SHAWKY',500,'300%')
per2=Employe(1,car1,'SHAWKE1234%@yahoo.com',5000,'Mah',500,'100%')
of =Office("name", per1)
of.get_all_employees()
#print(of.get_employee('MAHMOUD AHMED SHAWKY'))
of.fire('MAHMOUD AHMED SHAWKY')
of.deduct(70,10)
of.reward(1,20)
print(of.get_employee('MAHMOUD AHMED SHAWKY'))
of.get_all_employees()
#per1.drive(10)
#per1.refuel(100)
print(per1.work(10))

per1.car.run(20,100)


