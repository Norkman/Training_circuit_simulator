import json
import numpy as np
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import sys
import os

# Get the autorisation from google to extract sheets
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
json_file = os.path.abspath("autorisation.json")
creds = ServiceAccountCredentials.from_json_keyfile_name(json_file, scope)
client = gspread.authorize(creds)

# use numpy to extract all the data of the sheet
def extraction_of_sheet(name_of_sheet): # the input correspond to the name (string) of the sheet
    datas_of_sheet = np.array(client.open("Exercices").worksheet(name_of_sheet).get_all_values()) # get all the values of the sheets
    return datas_of_sheet

# extract differents sheets
def extract_data():
    data = extraction_of_sheet("Exercises")
    parameters = extraction_of_sheet("Parameters")
    np.save("parameters", parameters)
    np.save("data", data)

# select spécific row or column, the fonction find the parameter and extract its data
def extract_parameter(name_of_parameters, sheet): # the first input correspond to the name of the parameters, the second is all the data of the sheet
    loc_parameters = np.where(sheet == name_of_parameters) # find the location of the specific parameter
    if sheet[(0,0)] == "column" : # if the data of the parameters are presented in column
        int_loc_parameters = int(loc_parameters[1]) # transform the location to a number
        parameters_brut = sheet[:,int_loc_parameters][1:] # [:,int_loc_parameters] means you get all the value (:) of the column // [1:] means you put only the data from the value "1" until the end (:)
    
    elif sheet[(0,0)] == "row" : # if the data of the parameters are presented in row
        int_loc_parameters = int(loc_parameters[0])
        parameters_brut = sheet[int_loc_parameters,:][1:]

    else : # if the devloper omits to put 'row' or 'column' in the case (0,0) of the sheet
        print ("Error for developer :")
        print ("When you create a new sheet to extract, you have to write in case (0,0) 'row' or 'column'.")
        sys.exit()
    
    loc_of_null = np.where(parameters_brut == "") # find "null" values
    parameter = np.delete(parameters_brut, loc_of_null) # erase all values "null"
    return parameter

class DataParameters():
    def __init__(self):
        parameters = np.load('parameters.npy')
        self.time_of_workout = extract_parameter("Time_of_workout", parameters)
        self.difficulty_of_exercises = extract_parameter("Difficulty_of_exercises", parameters)
        self.part_of_body = extract_parameter("Part_of_body", parameters)
        self.equipment = extract_parameter("Equipment", parameters)
        self.type_of_wod =  extract_parameter("Type_of_wod", parameters)
        self.AMRAP_num_ex_per_block = extract_parameter("AMRAP_num_ex_per_block", parameters)
        self.AMRAP_num_block = extract_parameter("AMRAP_num_block", parameters)
        self.AMRAP_num_max_ex = int(extract_parameter ("AMRAP_num_max_ex", parameters))
        self.AMRAP_rest = int(extract_parameter("Rest_of_block", parameters))
        self.AMRAP_delta = int(extract_parameter("AMRAP_delta", parameters))
        self.full_body = int(extract_parameter("Full_Body", parameters))
        self.upper_body = int(extract_parameter("Upper_Body", parameters))
        self.lower_body = int(extract_parameter("Lower_Body", parameters))