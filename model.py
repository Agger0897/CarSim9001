from random import randint

class Car(object):
    pass

class Wheel(object):

    def __init__(self):
        self.orientation = randint(0,360)

    def rotate(self,revolutions):
        self.orientation = (self.orientation + (revolutions * 360))%360

#Hjul=Wheel()
#print(Hjul.orientation)
#Hjul.rotate(2.5)
#print(Hjul.orientation)

class Engine(object):
    pass


class Gearbox(object):

    def __init__(self):
        self.wheels = {'frontLeft':Wheel(),'frontRight':Wheel(), 'rearLeft':Wheel(),'rearRight':Wheel()} #dictionary
        self.currentGear = 0 #int
        self.clutchEngaged = False #Bool value
        self.gears = [0, 0.8, 1, 1.4, 2.2, 3.8] #list

    def shiftUp(self):
        if self.clutchEngaged == True and self.currentGear < len(self.gears)-1:
            self.currentGear = self.currentGear + 1

    def ShiftDown(self):
        if clutchEngaged == True and currentGear < 0:
            self.currentGear = self.currentGear - 1

    #def rotate




#g=Gearbox()
#for Wheel in g.wheels:
#    print(g.wheels[Wheel].orientation)

class Tank(object):

    def __init__(self):
        self.capacity = 100
        self.contents = 100

    def refuel(self):
        self.contents = self.capacity

    def remove(self,amount):
        self.contents = self.contents - amount
        if self.contents < 0:
            self.contents = 0


#tank=Tank()
#tank.remove(99)
#print(tank.contents)
