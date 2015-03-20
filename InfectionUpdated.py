import turtle
import random
import math




class Organism:

# -- Constructor -----------------------------------------------
    def __init__(self,iD, infection=1, origin=(0,0)):

        self.__infection= infection
        self.__location= (random.randint(-100,100), random.randint(-100,100))
        self.__visual=turtle.Turtle()
        self.__timer=0

        
        self.__visual.shape("turtle")
        self.__visual.shapesize(2,2)
        self.__visual.penup()
        self.__identity=iD
        self.__origin=origin


        
        
# -- Accessors -------------------------------------------------

    def diagnose(self):
        sickness= self.__infection
        return sickness
     

    def getLocation(self):
        return self.__location

    def getIdentity(self):
        return self.__identity
    


# -- Predicate -------------------------------------------------

    # Makes sure turtle stays in bounds
    # param xBoundary (tuple)- upper and lower limits of x boundary
    def xIsInBounds(self,xBoundary):
        return self.__location[0]>xBoundary[0] and self.__location[0]<xBoundary[1]
    
    # Makes sure turtle stays in bounds
    # param yBoundary (tuple)- upper and lower limits of y boundary
    def yIsInBounds(self,yBoundary):
        return self.__location[1]>yBoundary[0] and self.__location[1]<yBoundary[1]

    def isInProximity(self,other):
        location=other.getLocation()
        return self.__visual.distance(location)<50

    def isInCloseProximity(self,other):
        location=other.getLocation()
        return self.__visual.distance(location)<20

    def isDoctor(self):
        return self.__infection==0

    def isInfected(self):

        return self.__infection>1 and self.__infection<5

    def isContageous(self):

        return self.__infection>2 and self.__infection<5

    def isVeryContageous(self):

        return self.__infection==4

    def isHealthy(self):
        
        return self.__infection==1

    def isDead(self):

        return self.__infection>4
    
# -- Mutators --------------------------------------------------

    def makeBackground(self):
        self.__visual.shape("Globe.gif")


    def makeDoctor(self):
        self.__infection = 0
        self.__visual.shape("Doctor.gif")
        
 
        
        
    def infect(self):
        self.__infection = 2
        
    def contagious(self):
        self.__infection = 3
        
    def veryContagious(self):
        self.__infection = 4

    def heal(self):
        self.__infection = 1
        
    def timerIncrease(self):

        if self.__timer<10:
            self.__timer+=1
        
        elif self.__timer==10:
            self.__timer=0


    def infectionUpdate(self):

        if self.__infection>1:
            if self.__timer == 10:
                self.__infection += 1

    

    def setColor(self):

        if not self.isDoctor():
            
            if self.__infection==1:
                self.__visual.color("green")
                
            elif self.__infection==2:
                self.__visual.color("yellow")
                
            elif self.__infection==3:
                self.__visual.color("orange")
                
            elif self.__infection==4:
                self.__visual.color("red")
                
            else:
                self.__visual.shape("Tombstone.gif")


    def goto(self,x,y):
        self.__visual.goto(x,y)
        self.__location=x,y
    def reset(self):
        self.__visual.goto(origin)
        self.__location=0,0

    def locomote(self):

        

        if self.__visual.distance(self.__origin)<250:
            
                
                
            if self.__infection<5:
        
                newX=self.__location[0]+ random.randint(-30,30)
                newY=self.__location[1]+ random.randint(-30,30)

                self.__location= newX,newY

                

        else:
            spot = self.getLocation()
            origin = self.__origin
            newX= spot[0]
            newY= spot[1]
            
            
            if spot[0]<origin[0]:
                newX= spot[0]+15
            if spot[0]>origin[0]:
                newX= spot[0]-15
            if spot[1]<origin[1]:
                newY= spot[1]+15
            if spot[1]>origin[1]:
                newY= spot[1]-15

            self.__location= newX,newY

        self.__visual.goto(self.__location)


    def setshape(self):
        
        self.__visual.penup()
        self.__visual.shape("turtle")

    def viralTransmission(self,organismList):
                
        if self.isContageous():

            # interacts with nearby organisms      
            for otherItems in organismList:

                # If contageous, infects any healthy organism that is in close proximity
                if self.isContageous() and self.isInCloseProximity(otherItems) and otherItems.isHealthy():
                        otherItems.infect()
                                      
                # If "items" is in late stage, infects any healthy organism even in far proximity
                elif self.isVeryContageous() and self.isInProximity(otherItems) and otherItems.isHealthy():
                        otherItems.infect()
                        


    def medicalTreatment(self,organismList):

        if self.isDoctor():
                    
            # Cures organisms in proximity to doctor
            # interacts with nearby organisms      
            for otherItems in organismList:
    
                
                
                # checks if second object is the same as first.
                if not otherItems.isDoctor():
                    
                

                    # Heals ill organisms- doesn't effect doctors or fatalities
                    if self.isDoctor() and self.isInProximity(otherItems):

                        
                        if otherItems.diagnose()<5:
                            otherItems.heal()


def animate(organismList):


        for items in organismList:

            # Moves organism
            items.locomote()
            items.timerIncrease()
            items.infectionUpdate()
            items.setColor()
            items.viralTransmission(organismList)
            items.medicalTreatment(organismList)
            

def simulate(organismList):

        for items in organismList:

            # Moves organism
            #items.locomote()
            items.timerIncrease()
            items.infectionUpdate()
            items.setColor()
            items.viralTransmission(organismList)
            items.medicalTreatment(organismList)

            if items.isDead():
                organismList.remove(items)

            



def main():

    turtle.register_shape("Doctor.gif")
    turtle.register_shape("Tombstone.gif")
    turtle.register_shape("Globe.gif")
                                                    
                          
                                      

main()            
