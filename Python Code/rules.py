# import libraries
import os.path
import pandas as pd
from pandas.api.types import is_object_dtype, is_numeric_dtype, is_bool_dtype, is_string_dtype, is_float_dtype
import numpy as np
import re
import os.path
import traceback
from openpyxl import Workbook
import datetime
import argparse

def file_exists(file_location):
    if os.path.isfile(file_location)==False:
        print("Error Message: File doesn't exist")

##Import Company excel file
def import_data(file_location,error_log_name):
    with open(error_log_name, "a") as log:      
        try: 
            xl1 = pd.ExcelFile(file_location)  # Define the excel file
            worksheets = xl1.sheet_names  # Get the list of worksheets in the file
            found_dictionary, found_f_outputs = (False, False)
            dict_of_sheets = {}
            for sheet in worksheets:  # iterate through the sheets in the file
                if sheet.startswith("Dict_"):  # ...if the workseet starts with the text "Dict_" then...
                    found_dictionary=True
                    dict_of_sheets[sheet] = (pd.read_excel(xl1, sheet_name=sheet, skiprows=[0, 2]),"Dict_")               
                if sheet.startswith("fOut_"):  # ...if the workseet starts with the text "fOut" then...
                    found_f_outputs=True
                    dict_of_sheets[sheet] = (pd.read_excel(xl1, sheet_name=sheet, skiprows=[0, 2]),"fOut_")
            

            #Check if Exchel Sheet name exists        
            if not found_dictionary:
                print("Error message: A worksheet starting with 'Dict_' (a dictionary) was not found in worksheets", file=log)

            if not found_f_outputs:
                print("Error message: A worksheet starting with 'fOut_' (an F_Outputs sheet) was not found in worksheets", file=log)

        except Exception:
            traceback.print_exc(file=log)
            pass 
    return dict_of_sheets
    
    
##Import original excel file
def import_original_data(original_file_location,error_log_name):     
        try: 
            xl1 = pd.ExcelFile(original_file_location)  # Define the excel file
            worksheets = xl1.sheet_names  # Get the list of worksheets in the file
            original_dict_of_sheets = {}
            for sheet in worksheets:  # iterate through the sheets in the file
                if sheet.startswith("Dict_"):  # ...if the workseet starts with the text "Dict_" then...
                    original_dict_of_sheets[sheet] = (pd.read_excel(xl1, sheet_name=sheet, skiprows=[0, 2]),"Dict_")               
                if sheet.startswith("fOut_"):  # ...if the workseet starts with the text "fOut" then...
                    original_dict_of_sheets[sheet] = (pd.read_excel(xl1, sheet_name=sheet, skiprows=[0, 2]),"fOut_")
        except Exception:
            traceback.print_exc(file=log)
            pass 
            
        return original_dict_of_sheets

def timestamp_error_log(error_log_name):
    with open(error_log_name, "a") as log:      
        try: 
            # storing current date and time
            current_date_time = datetime.datetime.now().strftime("%d.%b %Y %H:%M:%S")
            print(f"\nThis file was created at: {current_date_time}\n",file = log)  
        except Exception:
            traceback.print_exc(file=log)
            pass
    

def fOut_headers_consistency(sheet_name,df,error_log_name):
## ---------------------------------------------------------------------
## *Headers* in spesific order and value. Headers are case insensitive
## ----------------------------------------------------------------------
    with open(error_log_name, "a") as log:
        try:
            print("\n________________________________________________________________________________________________________________________________________________________", file=log)
            print(f"\n*** Excel Sheet Name is: {sheet_name} ***\n"
                  "________________________________________________________________________________________________________________________________________________________", file=log)
            print(f"\n*** Data Validation Rule 1 *** Excel Sheet Name: {sheet_name} \n"
            "---------------------------------------------------------------------------------------------------------------------------------------------------------\n"
            "Headers in Excel file should be in specific order and value. Headers are case sensitive. \n"
            "---------------------------------------------------------------------------------------------------------------------------------------------------------\n",file = log)
            
            
            dictionary_errors_column_headers = {
                'Acronym': (df.columns[0], "Error message: 'Acronym' column name is not correct, please note name is case sensitive"),
                'Reference': (df.columns[1], "Error message: 'Reference' column name is not correct, please note name is case sensitive"),
                'Item description': (df.columns[2], "Error message: 'Item description' column name is not correct, please note name is case sensitive"),
                'Unit': (df.columns[3], "Error message: 'Unit' column name is not correct, please note name is case sensitive"),
                'Model': (df.columns[4], "Error message: 'Model' column name is not correct, please note name is case sensitive"),
           }
            
            error_counter=0
            for key, value in dictionary_errors_column_headers.items():
                if key==value[0]:
                    pass
                else:
                    error_counter+=1
                    print(value[1],file = log)         
            if error_counter==0:
                print("Success, No Errors detected!",file = log)
                return True 
            print(f"Please correct the header's names for this Excel Sheet: {sheet_name}, before data validation proceeds!",file = log) 
            return False
        except Exception:
            traceback.print_exc(file=log)
            return False

        
def regex_boncode(sheet_name,df,error_log_name):
##-------------------------------------------------------------------------------------------------------
##Boncode find pattern using *Regex*. Reference (BON code) should consist of the following in sequence: 
##An upper case letter. Zero or more upper case letters or underscores. 
## At least one digit. Zero or more number upper case letters, underscores, or digits. 
##No lower case letters. Boncodes must not contain "-" character.
##Note "str.fullmatch" doesn't work due to older python vesrion installed  
##-------------------------------------------------------------------------------------------------------
    with open(error_log_name, "a") as log:      
        try:  
            print(f"\n*** Data Validation Rule 2 *** Excel Sheet Name: {sheet_name} \n"
                  "---------------------------------------------------------------------------------------------------------------------------------------------------------\n"
                  "Boncode find pattern using *Regex*. Reference (BON code) should consist of the following in sequence: \n"
                  "An upper case letter. Zero or more upper case letters or underscores. At least one digit. Zero or more number upper case letters, underscores, or digits. \n"
                  "No lower case letters. Boncodes must not contain \- character.\n"
                  "---------------------------------------------------------------------------------------------------------------------------------------------------------\n",file = log)
            index=3 #index for showing cell position
            regex = r'^([A-Z][A-Z_]*[0-9]+[A-Z0-9_]*)$'  
            regex_pattern = re.compile(regex)
            error_counter=0
            for item in df['Reference']:
                index+=1 
                if pd.isna(item):
                    error_counter+=1
                    print(f"Error in Row {index}: 'Reference': {item}, 'Reference' is a mandatory field and cannot have empty values",file = log) 
                    break
                if bool(regex_pattern.match(item))==False:
                    error_counter+=1
                    print(f"Error in Row {index}: 'Reference': {item} doesn't match the regular expression",file = log)  
            if error_counter==0:
                print("Success, No Errors detected!",file = log)
        except Exception:
            traceback.print_exc(file=log)
            pass

def check_suffix(sheet_name,df,error_log_name):
## ---------------------------------------
## Checking *suffix _PR24* on Boncodes
## ---------------------------------------
    with open(error_log_name, "a") as log:
        try: 
            print(f"\n*** Data Validation Rule 3 *** Excel Sheet Name: {sheet_name} \n"
            "---------------------------------------------------------------------------------------------------------------------------------------------------------\n"
            "Reference (BON code) should have suffix _PR24\n"
            "---------------------------------------------------------------------------------------------------------------------------------------------------------\n",file = log)
            index=3 #index for showing row position
            suffix = "_PR24"
            error_counter=0
            
            for item in df['Reference']:   
                index+=1
                if pd.notna(item): 
                    if item.endswith(suffix):
                        pass
                    else: 
                        error_counter+=1
                        print(f"Error in Row {index}: Reference: {item} does not has a suffix _PR24",file = log)
            if error_counter==0:
                print("Success, No Errors detected!",file = log)
        except Exception:
            traceback.print_exc(file=log)
            pass
        
def check_data_type_unit(sheet_name,df,error_log_name):
## ------------------------------------------------------------------------------------------
##6. *Data Type Checking*. This verifies that the entered data has the appropriate data type. 
## ------------------------------------------------------------------------------------------
#Unit: Unit must be less than 21 characters.
    with open(error_log_name, "a") as log:
        try: 
            print(f"\n*** Data Validation Rule 4 *** Excel Sheet Name: {sheet_name} \n"
            "---------------------------------------------------------------------------------------------------------------------------------------------------------\n"
            "Data Type Checking. This verifies that the entered data has the appropriate data type \n"
            "Unit Column must be less than 21 characters \n"
            "---------------------------------------------------------------------------------------------------------------------------------------------------------\n",file = log)
            index=3 #index for showing row position
            error_counter=0
            unit_length=21
            
            for item1,item2 in zip(df['Unit'],df['Reference']):
                index+=1
                if type(item1) == int:
                    error_counter+=1
                    print(f"Error in Row {index}: Reference: {item2}: Unit must not be a number",file = log)            
                elif pd.notna(item1): 
                    if len(item1)>unit_length:
                        error_counter+=1
                        print(f"Error in Row {index}: Reference: {item2}: Unit must be <={unit_length} characters",file = log)
            if error_counter==0:
                print("Success, No Errors detected!",file = log)
        except Exception:
            traceback.print_exc(file=log)
            pass

def check_data_type_description(sheet_name,df,error_log_name):
#Description: Description must be less than 230 characters.
    with open(error_log_name, "a") as log:
        try: 
            print(f"\n*** Data Validation Rule 5 *** Excel Sheet Name: {sheet_name} \n"
            "---------------------------------------------------------------------------------------------------------------------------------------------------------\n"
            "Data Type Checking. This verifies that the entered data has the appropriate data type \n"
            "Description Column must be less than 230 characters \n"
            "---------------------------------------------------------------------------------------------------------------------------------------------------------\n",file = log)
            index=3       
            description_length=230
            error_counter=0
            
            for item1,item2 in zip(df['Item description'],df['Reference']):
                index+=1
                if pd.notna(item1):      
                    if len(item1)>description_length:
                        error_counter+=1
                        print(f"Error in Row {index}: Reference: {item2}: Description must be <={description_length} characters",file = log)
            if error_counter==0:
                print("Success, No Errors detected!",file = log)
        except Exception:
            traceback.print_exc(file=log)
            pass


def user_input(sheet_name,df,error_log_name):
    #---------------------------------------------------------------------
    ##Whether the values (e.g. anything under the years headers) corresponds to what is in the units columns
    #If the Unit value is not ‘Text’ the years columns values should be number 
    #---------------------------------------------------------------------  
    index=1 #index for showing row position
    predefined_unit=['%','£m','nr','kW','Ml','Ml/d','Propn 0 to 1','MWh','m.hd','Ml/day','km','mtrs','km2','Ml/yr','000s',
    '000\'s','l/h/d','£','l/d','hours','days','nr/000km','kg BOD5/day','ha','l/s','m3','m3/day','m2','m3/year',
    'year','ttds/ year','ttds*km/year','m3*km/yr','kg/d','kg Amm-N/d','ttds/yr','Index','£m, outturn',]

    index=2 #index for showing row position
    regex_columns=r'^([0-9]{4}-[0-9]{2})$' 
    regex_pattern = re.compile(regex_columns)


    with open(error_log_name, "a") as log:
        try:
            print(f"\n*** Data Validation Rule 6 *** Excel Sheet Name: {sheet_name} \n"
            "---------------------------------------------------------------------------------------------------------------------------------------------------------\n"
            "Input validation rule checks that values entered by the user are formatted correctly. \n"
            "For example, if Unit Column is named as Text, the user should enter a text \n"
            "---------------------------------------------------------------------------------------------------------------------------------------------------------\n",file = log)
            index=3
            error_counter=0
          
            for i, row in df.iterrows():
                index+=1
                
                for key in row.keys():
                    try:
                        if bool(regex_pattern.match(key)):
                            if row[key]=="##BLANK":
                                continue
                            elif row[key]==True:
                                continue
                            elif (row["Unit"] =="Time"):
                                continue
                            elif row[key]=="#DIV/0!":
                                continue
                            elif pd.isna(row[key]):
                                continue
                            elif row[key] == '\xa0':
                                continue
                            elif np.isnan(row[key]):
                                continue
                            elif pd.isna(row["Unit"]):
                                continue
                            #if unit is text and value in every column is not string
                            elif (row["Unit"].lower() in ["text"]) and type(row[key]) != str:
                                error_counter+=1
                                print(f"Error in Row: {index}, Reference: {df.loc[i, 'Reference']}, Column: {key}, Value: {row[key]}, " \
                                    "This is a text field, please check that your input is in text format", file=log)
                            #if unit is numeric, look at the list and value in every column is not int or float
                            elif row["Unit"] in predefined_unit and \
                                type(row[key])!=int and \
                                type(row[key])!=float:
                                    error_counter+=1
                                    print(f"Error in Row: {index}, Reference: {df.loc[i, 'Reference']}, Column: {key}, Value: {row[key]}, " \
                                        "This is a numeric field, please check that your input is in numerical format.", file=log)  
                    except Exception as e:
                        print(e, file=log)
            if error_counter==0:
                print("Success, No Errors detected!",file = log)
        except Exception as e:
            print(e, file=log)
            #traceback.print_exc(file=log)
            pass

def boncode_Consistency(sheet_name,dict_of_sheets,original_dict_of_sheets,error_log_name):

#-----------------------------------------------------------------------------------
#Boncode Consistency*, prevent accidental change/delete of Boncodes   
#-----------------------------------------------------------------------------------
    with open(error_log_name, "a") as log:
        try: 
            print(f"\n*** Data Validation Rule 7 *** Excel Sheet Name: {sheet_name} \n"
            "---------------------------------------------------------------------------------------------------------------------------------------------------------\n"
            "Boncode Consistency, Prevent accidental change and/or delete of Boncodes   \n"
            "Comparison between the original Boncodes versus the target Boncodes, where target Boncodes are those send by the companies after data submission.\n"
            "---------------------------------------------------------------------------------------------------------------------------------------------------------\n",file = log)
            amended_boncodes=dict_of_sheets['Reference']
            original_boncodes=original_dict_of_sheets['Reference']

            original_only_boncodes = list(set(original_boncodes) - set(amended_boncodes))  # The items in the original version, but not in ammended version
            if len(original_only_boncodes) > 0:
                print("Reference (Boncodes) in worksheet in the original version but not in the amended version: ",  *original_only_boncodes, sep="\n", file = log)
            else:
                print("Success, No Errors detected!",file = log)
        except Exception:
            traceback.print_exc(file=log)
            pass
