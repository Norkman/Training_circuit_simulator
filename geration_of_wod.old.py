from numpy.core.defchararray import array
from extraction import *
import random

def count_number_of_element_in_array(array, element) :
    find_element_in_structure = np.where(array == element)
    number_of_element = len(find_element_in_structure[0])
    return number_of_element


def simulate_structure(type_of_wod, part_of_body, parameters_sheet_data,time_of_wod):
    # Initialisation of variable
    mixte = "Mixte"
    upper_body = "Upper Body"
    lower_body = "Lower Body"
    full_body = "Full Body"
    part_of_body_name_of_parameter = part_of_body.replace(" ", "_")
    part_of_body_parameter = extract_parameter(part_of_body_name_of_parameter, parameters_sheet_data)


    wod = random.choice(type_of_wod)
    wod = "EMOM" #---------------------------------------delete

    if wod == "AMRAP":
        AMRAP_num_ex_per_block = extract_parameter("AMRAP_num_ex_per_block", parameters_sheet_data)
        AMRAP_num_block = extract_parameter("AMRAP_num_block", parameters_sheet_data)
        AMRAP_num_max_ex = int(extract_parameter ("AMRAP_num_max_ex", parameters_sheet_data))
        AMRAP_rest = int(extract_parameter("Rest_of_block", parameters_sheet_data))
        AMRAP_delta = int(extract_parameter("AMRAP_delta", parameters_sheet_data))

        while True :
            number_of_block_random = int(random.choice(AMRAP_num_block))
            number_of_exercises_per_block_random = int(random.choice(AMRAP_num_ex_per_block))
            number_of_exercises_random = number_of_exercises_per_block_random*number_of_block_random
            if number_of_exercises_random + AMRAP_rest <= AMRAP_num_max_ex and number_of_exercises_random + AMRAP_delta <= int(time_of_wod) and number_of_exercises_per_block_random + AMRAP_rest <= int(time_of_wod):
                number_of_block = number_of_block_random
                number_of_exercises_per_block = number_of_exercises_per_block_random
                number_of_exercise = number_of_exercises_random
                break
        
        while True :
            wod_structure = np.empty(0, dtype=int)
            for i in range(number_of_block) :
                for y in range(number_of_exercises_per_block) :
                    add_case_part_of_body = random.choice(part_of_body_parameter)
                    wod_structure = np.append(wod_structure, add_case_part_of_body)
                wod_structure = np.append(wod_structure, "Rest")
            wod_structure = np.delete(wod_structure , [len(wod_structure) - 1]) # erase the last element (rest) in the wod structure

            # find part of body in the wod structure create
            number_of_mixte = count_number_of_element_in_array(wod_structure, mixte)
            number_of_lower_body = count_number_of_element_in_array(wod_structure, lower_body)
            number_of_upper_body = count_number_of_element_in_array(wod_structure, upper_body)

            # condition 
            if part_of_body == full_body :
                if number_of_lower_body == number_of_upper_body and number_of_mixte <= int(number_of_exercise)/2 :
                    break
            
            elif part_of_body == lower_body :
                if number_of_exercise > number_of_lower_body and number_of_mixte <= int(number_of_exercises_per_block/2) and number_of_mixte != 0 :
                    break

            elif part_of_body == upper_body :
                if number_of_exercise > number_of_upper_body and number_of_mixte <= int(number_of_exercises_per_block/2) and number_of_mixte != 0 :
                    break
            else :
                continue

    if wod == "EMOM":

        EMOM_num_ex = extract_parameter("EMOM_num_ex", parameters_sheet_data)
        EMOM_num_cycle = extract_parameter("EMOM_num_cycle", parameters_sheet_data)
        EMON_delta = extract_parameter("EMON_delta", parameters_sheet_data)

        # initilaisation of variable
        time_random = 0
        while True :
            number_of_exercises_random = int(random.choice(EMOM_num_ex))
            number_of_cycle_random = int(random.choice(EMOM_num_cycle))
            time_random = number_of_exercises_random*number_of_cycle_random

            # to check error 
            print(" number of exercice : " + str(number_of_exercises_random) + " / number of cycle : " + str(number_of_cycle_random) + " / time : " + str(time_random))
            
            if time_random <= int(time_of_wod) and time_random >= (int(time_of_wod) - int(EMON_delta)) :
                number_of_exercises = number_of_exercises_random
                number_of_cycle = number_of_cycle_random
                break

        while True:
            wod_structure = np.empty(0, dtype=int)
            for i in range(number_of_exercises) :
                add_case_part_of_body = random.choice(part_of_body_parameter)
                wod_structure = np.append(wod_structure, add_case_part_of_body)
            
            # find part of body in the wod structure create
            number_of_mixte = count_number_of_element_in_array(wod_structure, mixte)
            number_of_lower_body = count_number_of_element_in_array(wod_structure, lower_body)
            number_of_upper_body = count_number_of_element_in_array(wod_structure, upper_body)

            # condition 
            if part_of_body == full_body :
                if number_of_lower_body == number_of_upper_body and number_of_mixte <= int(number_of_exercises/2) :
                    break
            
            elif part_of_body == lower_body :
                if number_of_exercises > number_of_lower_body and number_of_mixte <= int(number_of_exercises/2) and number_of_mixte != 0 :
                    break

            elif part_of_body == upper_body :
                if number_of_exercises > number_of_upper_body and number_of_mixte <= int(number_of_exercises/2) and number_of_mixte != 0 :
                    break
            else :
                continue

    return wod_structure, wod

def put_exercices_into_structure(wod_structure, difficulty, exercises_sheet_data, equipment_of_wod, parameters_sheet_data, time_of_wod):
    # initialisation of variable
    number_of_repetition = np.empty(0, dtype=int)
    wod_create = np.empty(0, dtype=int)

    num_of_rest_in_wod = count_number_of_element_in_array(wod_structure,"Rest")
    
    for i in range(len(wod_structure)):
        part_of_body_for_exercice = wod_structure[i].replace(" ","_") # for exemple replace "Lower body" by "Lower_Body" (the name of the parameters in sheet Exercices)
        if part_of_body_for_exercice == "Rest" :
            rest = int(extract_parameter("Rest_of_block", parameters_sheet_data))
            if int(time_of_wod) <= 15 :
                rest_in_secondes = (rest/num_of_rest_in_wod)
            else:
                rest_in_secondes = (rest/num_of_rest_in_wod)*2

            wod_create = np.append(wod_create, part_of_body_for_exercice)
            number_of_repetition = np.append(number_of_repetition, rest_in_secondes)

        else :
            specific_part_of_body = extract_parameter(part_of_body_for_exercice, exercises_sheet_data)
            specific_difficulty = extract_parameter(difficulty, exercises_sheet_data)
            exercises_name = extract_parameter("Exercises_name", exercises_sheet_data)


            while True :
                random_equipement_choosen = random.choice(equipment_of_wod) # one of equipement is choosen
                random_equipement_choosen = random_equipement_choosen.replace(" ","_")
                specific_equipment = extract_parameter(random_equipement_choosen, exercises_sheet_data)

                """
                # to check error 
                print(part_of_body_for_exercice, end=" <---> ")
                print(random_equipement_choosen)
                """

                # selection of exercice with all spécification  
                selected_number_of_repetition = np.empty(0, dtype=int)
                selected_exercises = np.empty(0, dtype=int)

                for j in range(len(exercises_name)) :
                    if specific_part_of_body[j] == "x" and specific_equipment[j] == "x" and specific_difficulty[j] != "0":
                        selected_exercises = np.append(selected_exercises, exercises_name[j])
                        selected_number_of_repetition = np.append(selected_number_of_repetition, specific_difficulty[j])

                if selected_exercises.size != 0 :
                    break
        
            """
            # verify the exercices selected by the programme
            print(selected_exercices, end=" <------------  ")
            print("\n")
            """
            # randomise choice of selected exercices and put in workout
            random_choice_of_exercises = random.choice(selected_exercises)
            wod_create = np.append(wod_create, random_choice_of_exercises)
            loc_repetion_of_selected_exercise = np.where(random_choice_of_exercises == selected_exercises) # find the location of the specific parameter
            int_loc_repetion_of_selected_exercise = int(loc_repetion_of_selected_exercise[0])
            number_of_repetition = np.append(number_of_repetition, selected_number_of_repetition[int_loc_repetion_of_selected_exercise])

    return wod_create, number_of_repetition, num_of_rest_in_wod

def show_wod(time_of_wod, wod, wod_create, number_of_repetition, num_of_rest_in_wod):
    print("You have to do a " + wod + " :\n")
    if wod == "AMRAP":

        for i in range(len(wod_create)):
            if wod_create[i] == "Rest" :

                # calculate the time of a block
                number_of_block = num_of_rest_in_wod + 1
                time_of_practice = float(time_of_wod) - float(number_of_repetition[i])
                time_of_block_float = time_of_practice/number_of_block
                time_of_block = round(time_of_block_float)

                # calculate the rest between two blocks
                rest = str(float(number_of_repetition[i])*60)

                if time_of_block_float % time_of_block > 0.5 or time_of_practice + num_of_rest_in_wod*float(rest) > float(time_of_wod):
                    time_of_block = time_of_block - 0.5

                print("---- during " + str(time_of_block) + " min ----")
                print("\n---- Rest during " + rest + " secondes ----\n")
            else :
                print(" - " + number_of_repetition[i] + " x " + wod_create[i])
        
        if count_number_of_element_in_array(wod_create, "Rest") == 0 :
            print("---- during " + time_of_wod + " min ----")
        else :
            print("---- during " + str(time_of_block) + " min ----")
    
    if wod == "EMOM" :
        time_of_wod = round(float(time_of_wod)/len(wod_create))
        for i in range(len(wod_create)):
            print(" - " + number_of_repetition[i] + " x " + wod_create[i])
        print("---- " + str(time_of_wod) + " times ----")
    
    print("\nGood luck ! ;)")