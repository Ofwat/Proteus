import os
import sys
import datetime
from rules import file_exists, fOut_headers_consistency, import_data, import_original_data, regex_boncode, timestamp_error_log, check_suffix, check_data_type_unit, check_data_type_description, user_input, boncode_Consistency

def main(dict_of_sheets, original_dict_of_sheets, error_log_name):
    with open(error_log_name, "a") as log:      
        try: 
            for key, value in dict_of_sheets.items():
                if value[1]=="fOut_":        
                    if fOut_headers_consistency(key,value[0],error_log_name):  #Rule  1
                        regex_boncode(key,value[0],error_log_name) #Rule 2
                        check_suffix(key,value[0],error_log_name) #Rule 3 
                        check_data_type_unit(key,value[0],error_log_name) #Rule 4
                        check_data_type_description(key,value[0],error_log_name) #Rule 5
                        user_input(key,value[0],error_log_name) #Rule 6
                        boncode_Consistency(key,value[0],original_dict_of_sheets[key][0],error_log_name) #Rule 7
        except Exception:
            traceback.print_exc(file=log)
            pass 

if __name__ == "__main__":
    
    file_location = input("Enter filename(full path): ")
    error_log_name = ("Error log_"+datetime.datetime.now().strftime("%d.%m.%Y %H.%M")+".txt")
    
    if not file_location.isalpha():
        file_location = str(file_location)
        
    if not os.path.exists(file_location):
        print(f"File location: {file_location} is invalid. Please provide a valid file location.")
        sys.exit()
    
    original_file_location ='Comparion_PR24.xlsx'
  

     ## Functions to execute 
    timestamp_error_log(error_log_name)
    dict_of_sheets={}
    dict_of_sheets=import_data(file_location,error_log_name)
    original_dict_of_sheets={}
    original_dict_of_sheets=import_original_data(original_file_location,error_log_name)
    main(dict_of_sheets,original_dict_of_sheets,error_log_name)
        
     