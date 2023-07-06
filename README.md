# Proteus

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#Setup)
* [How to Run Python Script Using the Command-Line without using .exe file](#How-to-Run-Python-Script-Using-the-Command-Line-without-using-.exe-file)
* [How to download Proteus.exe from Github](#How-to-download-Proteus.exe-from-Github)
* [License](#License)
* [Contributing](#Contributing)
* [Contact](#Contact) 

## General info
Proteus is a data validation and verification software application that helps ensure that collected data reflects its intended purpose. The application checks that data in the destination file (a company's set of business plan tables) matches certain expectations.  
The tool automatically performs a level of verification of the populated data, matching all the records and flagging exceptions. 
The Proteus application should be run after populating with data version 5 of the business plan table template. 
	
## Technologies
The project is created with:
* Python 3.7.3
* pyinstaller 5.12.0
	
## Setup
To run this project, you will need to download :  
1. Comparison template: This is version 5 of the business plan table template published on our website. It does not contain any user input. This file is used as the basis of comparison with a company's set of business plan tables. The Excel file name is: Comparion_PR24.xlsx. 
2. Populated template: This is the 'comparison template' although it should contain user input. Please fill in all the relevant sheets before running the application. 
3. Proteus.exe: The .exe file is a Windows-specific executable file format. When the user triggers it, the computer runs the code that the file contains.

The steps to run .exe are as follows:  

1. Download the Proteus.exe file and the comparison template. Store the above files and the populated template in the same folder.  
2. The comparison template file name is case sensitive. It is essential not to make any changes to this file.   
3. After data population save the populated template in the file format (.xlsx). To do so open the workbook you want to save. Click File > Save As. Pick the place where you want to save the workbook. For example, select Computer to save it in a local folder where Proteus.exe and Comparison template is also saved. In the Save as type list, click the file format Excel Workbook (*.xlsx).  
4. Double-click the Proteus.exe file to run it. This brings up a console that asks user input filename of the data on which they wish to run the data validation rules. 
5. The message that the user should see on the Windows Command Prompt is: "Enter filename (full path)".  
6. Add the full (absolute) path of the [populated template] and press Enter to run the file. (A full path refers to the complete details needed to locate a file or folder, starting from the root element, and ending with the other subdirectories). For example, a full path is: C:\Users\Maria.diapouli\OneDrive -OFWAT\Python\validation_tool\original\company_RP24_BP_tables_v5.03.xlsx 
7. Once the user has entered the file's name, the console will close. 
8. If the application runs successfully, the user will see an error log file in the same folder. Please look at the "Example of Error Log file .txt" as an indicator on what this error log file would look like, if no errors are detected.  
9. Open the Error Log File to view the results of the data validation rules. (If the application couldn't run then the error log file will be empty. There is no information to display.) 
10. At the beginning of the file there is a timestamp showing when the error log was created. Every time the application runs a new version of error log file is created.

## How to Run Python Script Using the Command-Line without using .exe file

1. Download Proteus.py, rules.py, Comparison template: named: Comparion_PR24.xlsx and Populated template: named: V5 PUBLISH
2. After data population save the populated template in the file format (.xlsx). To do so open the workbook you want to save. Click File > Save As. Pick the place where you want to save the workbook. For example, select Computer to save it in a local folder where Proteus.exe and Comparison template is also saved. In the Save as type list, click the file format Excel Workbook (*.xlsx).  
3. Store the above four files in the same folder. 
4. The user needs to install python or Anaconda Python platform in their machine. Anaconda Python allows you to write and execute code in the programming language Python. !The rest of the instructions applied if you have Anaconda Python platform installed in your machine.
5. To open Anaconda Prompt: Go to Windows: Click Start, search for Anaconda Prompt, and click to open.
6. Go to the location where the Proteus.py file is stored.
7. Right-click the Proteus.py file. Properties: Click this option to immediately view the full file path (Location).
8. Type ```cd [full file path]```
9. Type in the word ```python Proteus.py``` and press Ender
10. An Error log file will be created in the same location where Python.py exists

## How to download Proteus.exe from Github

1. Select the 'Proteus' repository on GitHub
2. Click on the 'proteus.exe' tab 
3. In the center of the screen click on 'view raw'
4. Your computer should be downloading the file - save the file in your desired location
5. The file is saved with a '.crdownload' file extension.  This is a temporary file extension used by the web browser.
6. Rename it to 'Proteus.exe'. Without renaming the file you cannot run the application.
7. A dialogue box will appear asking you to confirm your changes. Select ok.
8. The .exe file should be ready to open.
   
## License
Distributed under the Open Goverment License. See [LICENSE.txt](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/ for more information.

## Contributing
If you have a suggestion that would make this better, pleace contact:
PR24@ofwat.gov.uk ,
maria.diapouli@ofwat.gov.uk ,  
alex.whitmarsh@gov.uk

## Contact
* Lead Developer: Maria Diapouli: maria.diapouli@ofwat.gov.uk
* Quality Assurance: Alex Whitmarsh: Alex.Whitmarsh@ofwat.gov.uk
