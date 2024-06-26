## ENDG 233 Fall 2023
## Portfolio Project 1
## rover.py
## Program for calculating the time it takes a rover to travel depending on rover parameters and storm status.
## Muaz Bin Saad


## This module can be used to access math.floor() and math.ceil() as needed.
## e.g. math.floor(10/3) = 3, math.ceil(10/3) = 4
import math

## Tip: Create constants that can be used to store the rover parameters.
## Units should be indicated in comments
## e.g.  battery_1 = 100         ## 100 kWh



## BEGIN CODE HERE

battery_capacity=1 ##Initalising. Since they get defined in the if, so if the number is not 1 to 3 i want it to have some value to avoid 'not defined' errors and 'dividing by zero' errors.
battery_efficiency=1
solar_capacity=1
velocity=1

rover_validity=True ##initally the rover choice is valid 
rover_choice=int(input('Which rover would you like to move? (Number from 1 to 3): '))## user enters details
distance=int(input('How far is the mission in km? '))
storm_condition=input('Is there a storm in the forecast (True or False)? ')
if rover_choice==1: ##if charlie is chosen assign these specs
    ##depending on which rover they chose the specifications for its battery etc. will be assgined uniquely
    battery_capacity=100 ##100kWh
    battery_efficiency=50/100 ##50kWh/100km
    solar_capacity=5 ##5kW
    velocity=5 ##5km/hr
elif rover_choice==2: ##if alpha is chosen assign these specs
    battery_capacity=130 ##130kWh
    battery_efficiency=40/100 ##40kWh/100km
    solar_capacity=8 ##8kW
    velocity=4 ##4km/hr
elif rover_choice==3:##if november is chosen assign these specs
    battery_capacity=80 ##80kWh
    battery_efficiency=30/100 ##30kWh/100km
    solar_capacity=4 ##4kW
    velocity=6 ##6km/hr
else:
    rover_validity= False ##since a number instead of 1 2 or 3 is chosen, therefore the choice isnt valid and will output that in the end. and basically no calculations will happen since the values all =1. 

##CALCULATIONS
distance_per_charge=(battery_capacity/battery_efficiency) ##100/(50/100)=200km 
amount_of_charges=math.ceil(distance/distance_per_charge) ##rounds up because it will charge to  a hundred percent each time.
amount_of_charges=amount_of_charges-1 ##subtract 1 because has full charge at the start so, not needed an initall charge. 
##I could remove the -1 and +1 but for clarity its there.
charging_time=battery_capacity/solar_capacity ##time to charge to 100%
total_charge_time=amount_of_charges*charging_time ##accounts for how many times it needs to charge and calculates that total time
travel_time=distance/velocity ## This is the time it would take to travel said distance
total_time=travel_time+total_charge_time ##This is the total time, combining the trips time and the amount of time taken in charging.

if storm_condition=='True':
    total_time=total_time*1.2 ##the program does the next step regardless of condiiton, but total time will be 1.2 times more if the condition of the storm is true. This is not a boolean, since this is based on input, so it is a string.
if rover_validity==False:##if not between 1 to 3, outputs 
    print('Rover number not recognized')
elif rover_validity==True:##if its between 1 to 3 then it outputs the calculation results
    print(f'The total travel time for Rover {rover_choice} to travel {distance:.1f} km is {total_time:.1f} hours.')
