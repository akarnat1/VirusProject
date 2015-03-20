'''
Rafi Schulman
rschulm4@binghamton.edu
Anthony Karnati
akarnat1@binghamton.edu
CS 110
Final Project
5/8/14
'''

'''
The ViusSimGUI class, simulates the spread of a virus
  as well as the prevention and possible reversal of a virus.
It implements both tkinter and turtle to perform the simulation.
Output:
  turtle window (turtle)
Input:
  user presses buttons (tkinter)
Classes Used:
  Organims(InfectionUpdated)
  VirusSimGUI(VirusSimGUI)
'''


#imports--------------------------------------------------------------------
from tkinter import *
from InfectionUpdated import *
from counterWP2 import *
import turtle



class VirusSimGUI:
      #Constructor----------------------------------------------------------
      '''This will set up the tkinter window, add the buttons and
      open up the turtle window as well.'''
      def __init__(self): 
            self.__organisms=[]
            #open up tkinter window
            self.__win=Tk()
            #keeps count of organisms
            self.__win.title("Welcome to the Virus Simulator")
            self.__counter=CounterWP()
            #sets up background
            self.__background=Organism(self.__counter)
            self.__background.makeBackground()
            #keeps track of number of loops
            self.__loopTracker=0
            #stop animation button
            self.__haltAnimation=Button(self.__win,\
                                      text='Stop Animation',\
                                      command=self.haltAnimation)
            self.__haltAnimation.pack(side='right')
            #add healthy organism button
            self.__addOrganism=Button(self.__win,\
                                      text='Add an Organism',\
                                      command=self.addOrganism)
            self.__addOrganism.pack(side='left')
            #add infected organism button
            self.__addInfectedOrganism=Button(self.__win,\
            text='Add an Infected Organism',\
            command=self.addInfectedOrganism)
            self.__addInfectedOrganism.pack(side='left')
            #Animate simulation button
            self.__animateButton=Button(self.__win,\
            text='Animate the Simulation',\
            command=self.animateOrganisms)
            self.__animateButton.pack(side='right')
            #add a doctor button
            self.__addDoctor=Button(self.__win,\
            text='Add a doctor to the Population',\
            command=self.addDoctor)
            self.__addDoctor.pack(side='right')
            #add a contagious organism button
            self.__addContagiousOrganism=Button(self.__win,\
            text='Add an contagious organism',\
            command=self.addContagiousOrganism)
            self.__addContagiousOrganism.pack(side='left')
            #add a very contagious organism
            self.__addVeryContagiousOrganism=Button(self.__win,\
            text='Add an extremely contagious organism',\
            command=self.addVeryContagiousOrganism)
            self.__addVeryContagiousOrganism.pack(side='right')
           
            #listener
            mainloop()

      #Mutators-------------------------------------------------------------
      #This function stops the animation     
      def haltAnimation(self):

            self.__loopTracker=1

            
      #This function adds a healthy organism
      def addOrganism(self):
            
            self.__counter.increment()
            
            healthy=Organism(self.__counter)
            healthy.setColor()
            print(healthy.getIdentity())
            healthy.locomote()
            self.__organisms.append(healthy)
      #This function adds a doctor   
      def addDoctor(self):
            
            self.__counter.increment()
            
            doc=Organism(self.__counter)
            doc.makeDoctor()
            doc.setColor()
            doc.locomote()
            print(doc.getIdentity())
            self.__organisms.append(doc)
      #This function adds an infected organism  
      def addInfectedOrganism(self):
            
            self.__counter.increment()
            
            infected=Organism(self.__counter)
            infected.infect()
            infected.setColor()
            print(infected.getIdentity())
            infected.locomote()
            self.__organisms.append(infected)
            
      #This function adds a contagious organism
      def addContagiousOrganism(self):
            self.__counter.increment()
            
            contagious=Organism(self.__counter)
            contagious.contagious()
            contagious.setColor()
            contagious.locomote()
            self.__organisms.append(contagious)

      #This function adds a very contagious organism
      def addVeryContagiousOrganism(self):
            self.__counter.increment()
            veryContagious=Organism(self.__counter)
            veryContagious.veryContagious()
            veryContagious.setColor()
            veryContagious.locomote()
            self.__organisms.append(veryContagious)
      #This function animates the simulation
      def animateOrganisms(self):

            self.__loopTracker=0
            
            while self.__loopTracker==0:
              
              animate(self.__organisms)
      
           

#invokes class
VirusSimGUI()            
