'''
The Wellness Project 

File 1: Wellness_Project.py

from Wellness import *

# Variable declarations
total_steps = 0
total_miles = 0
total_water = 0

# Create the WellnessApp class
class WellnessApp:
    
    # Constructor for the WellnessApp class
    def __init__(self):
        self.steps = 0
        self.miles = 0
        self.water = 0
    
    # Method to update the total amount of steps
    def updateSteps(self, newSteps):
        global total_steps
        self.steps = newSteps
        total_steps += newSteps
    
    # Method to update the total miles
    def updateMiles(self, newMiles):
        global total_miles
        self.miles = newMiles
        total_miles += newMiles
    
    # Method to update the total water intake    
    def updateWater(self, newWater):
        global total_water
        self.water = newWater
        total_water += newWater
    
# Create a Wellness object
WellnessProject = WellnessApp()

# Set the initial values for the Wellness object
WellnessProject.updateSteps(5000)
WellnessProject.updateMiles(25)
WellnessProject.updateWater(8)

# Print out the total number of steps, miles, and water
print("Total steps taken: " + str(total_steps))
print("Total miles traveled: " + str(total_miles))
print("Total water intake: " + str(total_water))

# Set the goal values for the Wellness object
WellnessProject.updateSteps(10000)
WellnessProject.updateMiles(50)
WellnessProject.updateWater(16)

# Print out the goal values
print("Goal steps taken: " + str(total_steps))
print("Goal miles traveled: " + str(total_miles))
print("Goal water intake: " + str(total_water))

'''

File 2: Wellness.py

# Class for the WellnessApp
class WellnessApp:
    
    # Constructor for the WellnessApp class
    def __init__(self):
        self.steps = 0
        self.miles = 0
        self.water = 0
    
    # Method to update the total amount of steps
    def updateSteps(self, newSteps):
        self.steps = newSteps
    
    # Method to update the total miles
    def updateMiles(self, newMiles):
        self.miles = newMiles
    
    # Method to update the total water intake    
    def updateWater(self, newWater):
        self.water = newWater