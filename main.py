from extraction import *
from generation_of_wod import *
from structure import *

# Extract differents sheets, enable if data update
# extract_data()

# Extract parameters of the sheet "parameters"

parameters = DataParameters()
wod = Wod()
# np.load("")
# Time of workout
wod.time = parameters.time_of_workout[0]

# Dificuty of the workout
wod.difficulty = parameters.difficulty_of_exercises[0]

# Part of the body
wod.part = parameters.part_of_body[0]
if wod.part == "Full Body" :
    wod.part = parameters.full_body
elif wod.part == "Upper Body" :
    wod.part = parameters.upper_body
elif wod.part == "Lower_Body" :
    wod.part = parameters.lower_body

# Chose equipment
equipments = []
# choices = [0, 2, 5]
choices = []
if choices == [] :
    equipments = "No_equipment"
    
else :
    for equipment in choices :
        equipments.append(parameters.equipment[equipment])    
        
wod_structure, wod = simulate_structure(parameters, wod)