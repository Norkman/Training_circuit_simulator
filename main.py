from extraction import *
from geration_of_wod import *

# Extract differents sheets, enable if data update
# extract_data()

# Extract parameters of the sheet "parameters"

parameters = DataParameters()
np.load("")
# Time of workout
time_of_wod = parameters.time_of_workout[0]

# Dificuty of the workout
difficulty = parameters.difficulty_of_exercises[0]

# Part of the body
part = parameters.part_of_body[0]
if part == "Full Body" :
    part = parameters.full_body
elif part == "Upper Body" :
    part = parameters.upper_body
elif part == "Lower_Body" :
    part = parameters.lower_body

# Chose equipment
equipments = []
# choices = [0, 2, 5]
choices = []
if choices == [] :
    equipments = "No_equipment"
    
else :
    for equipment in choices :
        equipments.append(parameters.equipment[equipment])    
        
wod_structure, wod = simulate_structure(parameters, part, time_of_wod)