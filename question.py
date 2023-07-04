from verify import*
import numpy as np
"""
"""
def ask_question(parameter, something): # the variable something is to put a string in the end of print (for exemple put "minutes" at the end when the programm ask a question relative to time)
    for i in range(len(parameter)): # use a for loop to show to the user the data of the specific parameter
        print("- Enter " + str(i+1) + " for " + parameter[i] + something) # str(i+1) allows the variable 'i' to be a char 
        # we add 1 to 'i' for to avoid presenting a "zero" value to the user
    print("Enter the index : ", end="")

def ask_yes_or_no():
    print("- Tape -y for yes\n- Tape -n for no")
    end_of_loop = False
    while end_of_loop == False :
        print("Your choice : ", end="")
        input_yes_or_no = input() # waiting the input of the user
        print("\n")
        if input_yes_or_no == "n" or input_yes_or_no == "no" or input_yes_or_no == "No" or input_yes_or_no == "NO" :
            end_of_loop == True
            return "no"
        elif input_yes_or_no == "y" or input_yes_or_no == "yes" or input_yes_or_no == "Yes" or input_yes_or_no == "YES" :
            end_of_loop == True
            return "yes"
        else :
            print("You have only tape -y for yes or -n for no")

def ask_equipements(equipment):
    print("Choose your equipment :")
    # input_equipment_choice = np.empty([0], dtype=int)
    equipment_of_wod = np.array("No_equipment")
    end_of_loop = False
    while end_of_loop == False :
        for i in range(len(equipment)):
            ask_question(equipment, "")
            input_equipment = verify_input_of_user(equipment, "equipment")
            equipment_of_wod = np.append(equipment_of_wod, equipment[input_equipment])
            equipment = np.delete(equipment, input_equipment) # delete the selection of the user to avoid to choose a second time the same equipment
            if (len(equipment)==0) : # if all equipments are choosen, stop the loop
                end_of_loop = True
                break
            print ("You want to add an other equipment ?")
            answer = ask_yes_or_no()
            if answer == "yes" :
                end_of_loop = False
            elif answer == "no" :
                end_of_loop = True
                break
    return equipment_of_wod




