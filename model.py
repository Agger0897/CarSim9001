from random import randint

class Car(object):

    def __init__(self):
        self.theEngine = Engine()         #Reference til klassen engine

    def updateModel(self,dt):
        self.theEngine.updateModel(dt)    #Kører updatemodel funktionen med parameteren DeltaTime

class Wheel(object):

    def __init__(self):
        self.orientation = randint(0,360) #Tildeler hjulets orientering en værdi mellem 0 og 360

    def rotate(self,revolutions):
        #Udregner hjulets nye postition ud fra antallet af omdrejninger
        #Gøres ved at ligge hjulets nuværende position sammen med antallet af omdrejninger i grader
        #Derefter bruges modulo til at finde hjulets nye postition
        self.orientation = (self.orientation + (revolutions * 360))%360

class Engine(object):

    def __init__(self):
        self.throttlePosition = 0           #Int
        self.theGearbox = Gearbox()         #Reference til klassen Gearbox
        self.currentRpm = 0                 #Int
        self.maxRpm = 100                   #Int
        self.consumptionConstant = 0.0025   #Float
        self.theTank = Tank()               #Reference til klassen Tank

    def updateModel(self,dt):
        if self.theTank.contents > 0: #Hvis der er noget i tanken
            #Gør motorens omdrejningstal til at være hvor meget speederen er trykket ned ganget med det maksimale omdrejningstal
            self.currentRpm = self.throttlePosition * self.maxRpm
            #Fjern en mængde fra tanken, svarende til motorens nuværende omdrejningstal ganget med brændsstofsforbrugs konstanten
            self.theTank.remove(self.currentRpm * self.consumptionConstant)
            #Roter hjulene i dictionariet self.wheels
            self.theGearbox.rotate(self.currentRpm*(dt/60))

        elif self.theTank.contents <= 0:                      #Hvis nu er tanken er tom (eller mindre)
            self.currentRpm = 0                               #Sæt motorens nuværende omdrejningstal til 0
            self.theGearbox.rotate(self.currentRpm*(dt/60))   #Roter hjulene i dictionariet self.wheels

class Gearbox(object):

    def __init__(self):
        self.wheels = {'frontLeft':Wheel(),'frontRight':Wheel(), 'rearLeft':Wheel(),'rearRight':Wheel()} #Dictionary
        self.currentGear = 0                      #Int
        self.clutchEngaged = False                #Bool value
        self.gears = [0, 0.8, 1, 1.4, 2.2, 3.8]   #List

    def shiftUp(self):
        if self.currentGear < len(self.gears)-1 and not self.clutchEngaged:    #Hvis det nuværende gear er mindre end længden af alle gearne og koblingen er aktiveret
            self.currentGear += 1                                              #Sæt nuværende gear 1 op

    def shiftDown(self):
        if self.currentGear > 0 and not self.clutchEngaged:    #Hvis det nuværende gear er over 0 og koblingen er aktiveret
            self.currentGear -= 1                              #Sæt nuværende gear 1 ned


    def rotate(self,revolutions):
        if self.clutchEngaged == True:  #Hvis koblingen er aktiveret
            for wheel in self.wheels:   #Løkke for hver instans af hjul i dictionariet
                self.wheels[wheel].rotate(revolutions * self.gears[self.currentGear]) #Roterer hjul med omdrejninger ganget med det nuværende gear

class Tank(object):

    def __init__(self):
        self.capacity = 100     #Variable for tankens størrelse
        self.contents = 100     #Variable for tankens indhold

    def refuel(self):
        self.contents = self.capacity   #Tankens størrelse bliver til tankens indhold

    def remove(self,amount):                       #Definerer funktionen remove, med paramteren amount
        self.contents = self.contents - amount     #Variablen opdateres, til at der trækkes en mængde fra tankens indhold
        if self.contents < 0:                      #Hvis tankens indhold er under 0
            self.contents = 0                      #Sættes tankens indhold til 0

# g=Tank()
# print(g.contents)
