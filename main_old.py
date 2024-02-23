from question import *
from extraction import *
from verify import *
from generation_of_wod import *
import oauth2client


# Extract differents sheets 
exercises_sheet_data = extraction_of_sheet("Exercises")
parameters_sheet_data = extraction_of_sheet("Parameters") 

# Extract parameters of the sheet "parameters"
time_of_workout = extract_parameter("Time_of_workout", parameters_sheet_data)
difficulty_of_exercises = extract_parameter("Difficulty_of_exercises", parameters_sheet_data)
part_of_body = extract_parameter("Part_of_body", parameters_sheet_data)
equipment = extract_parameter("Equipment", parameters_sheet_data)
type_of_wod =  extract_parameter("Type_of_wod", parameters_sheet_data)


#----------------------------------------------FOR TEST PROGRAMM----------------------------------------------------------------

#----------------------------------------------FOR TEST PROGRAMM----------------------------------------------------------------

# Ask the time of the workout
print("How much time do you have for your workout ? ")
ask_question(time_of_workout, " minutes")
input_time = verify_input_of_user(time_of_workout, "time")
time_of_wod = time_of_workout[input_time]

# Ask the dificuty of the workout
print("Choose your difficulty :")
ask_question(difficulty_of_exercises, "")
input_dificulty = verify_input_of_user(difficulty_of_exercises, "difficulty")
difficulty = difficulty_of_exercises[input_dificulty]

# Ask the part of the body
print("Choose the part of the body you want to work on :")
ask_question(part_of_body, "")
input_part = verify_input_of_user(part_of_body, "part of body")

#Ask the type of equipement
print("Have you got equipment(s) ?")
answer_yes_or_no = ask_yes_or_no()
if answer_yes_or_no == "no" :
    equipment_of_wod = np.array(["No_equipment"])
elif answer_yes_or_no == "yes" :
    equipment_of_wod = ask_equipements(equipment)

"""
print("\n----verficitaion for developpers----- ")
print("- Time --> " + time_of_wod)
print("- Difficulty --> " + difficulty)
print("- Part of the body --> " + part)
print("- Equipment --> ", end="")
print (equipment_of_wod)
"""

max = 100

for i in range(max) :
    wod_structure, wod = simulate_structure(type_of_wod, part, parameters_sheet_data, time_of_wod) 
    #print(wod_structure)
    wod_create, number_of_repetition, num_of_rest_in_wod = put_exercices_into_structure(wod_structure, difficulty, exercises_sheet_data, equipment_of_wod, parameters_sheet_data, time_of_wod)
    #print(wod_create)
    show_wod(time_of_wod, wod, wod_create, number_of_repetition, num_of_rest_in_wod)
    print("\n")