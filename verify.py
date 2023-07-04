def verify_input_of_user(parameter, name_of_parameter):
    is_correct = False 
    count_miss = len(parameter)
    while is_correct == False or count_miss == len(parameter):
        count_miss = 0
        answer = input()
        if (answer.isdigit()):
            if int(answer)-1 < len(parameter) and int(answer)-1 >= 0:
                answer_name = parameter[(int(answer)-1)]
                for i in range(len(parameter)):
                    if answer_name != parameter[i] or parameter[i] == "" or answer_name == "":
                        count_miss = count_miss + 1
            if count_miss == len(parameter)-1:
                answer_in_number = int(answer)
                print("\n")
                is_correct = True
            elif (count_miss != len(parameter)-1):
                print("\nPlease choose a correct idex for the " + name_of_parameter + " !")
                print("Enter your " + name_of_parameter + " :", end="")
                is_correct = False
        elif (answer == ""):
            print("\nYou have to do a choice !")
            print("Enter your " + name_of_parameter + " :", end="")
            is_correct = False
        else:
            print("\nYou have to input a number !")
            print("Enter your " + name_of_parameter + " :", end="")
            is_correct = False
    return answer_in_number - 1