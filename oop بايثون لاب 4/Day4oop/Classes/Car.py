class Car:
    def __init__(self,name,fuelRate,velocity):
        self.name=name
        self.fuelRatee = fuelRate
        self.velocityy = velocity
    def run(self,velocity,distance):
        self.fuelRate -=0.5
        self.velocityy=velocity

        print("CAR IS RUNNING NOW WITH", velocity)
        if self.fuelRate ==0 or velocity ==0:
            Car.stop(self)

    def stop(self):
        print("CAR IS STOPING NOW" ,self.name)

    @property
    def velocity(self):
        return self.velocity

    @velocity.setter
    def velocity(self, velcoity):
        if (velcoity <= 200):
            self.velocityy = velcoity
        else:
            print("cant Be")


    @property
    def fuelRate(self):
        return  self.fuelRatee

    @fuelRate.setter
    def fuelRate(self, fuelrate):
        if (fuelrate <= 100):
            self.fuelRatee = fuelrate
        else:
            print("cant Be")





