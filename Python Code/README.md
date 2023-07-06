#  How to create a .exe file (Proteus.exe) as a developer

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#Setup)
* [PyInstaller Artifacts](#PyInstaller-Artifacts) 
* [.Exe limitations](#.Exe-limitations) 
* [License](#License)
* [Contributing](#Contributing)

## General info
Here you can find details on how to create an executable in Python Using PyInstaller
	
## Technologies
Project is created with:
* Python 3.7.3
* pyinstaller 5.12.0
	
## Setup
### Preparing Your Project

1. Install Pyinstaller. You can do this using pip like other Python packages:
```$ pip install pyinstaller```
  PyInstaller requires your application to conform to some structure. 
  Create an entry-point script named Proteus.py that imports your packages in our case rules.py and runs main(). 
  The first step to building an executable version of the project is to have the entry-point script.
2. Download the Proteus.py, rules.py scripts, Proteus.spec, Comparison template.xlsx, Populated template.xlsx
3. Store the above files five files in the same folder.  
4. From the Start menu, search for and open the Anaconda Command Prompt.
5. Type cd, a space, and then the location where .py files are stored For example in my case is: cd C:\Users\Maria.diapouli\OneDrive - OFWAT\Python\validation_tool\original\
6. Type ```pyinstaller  --onefile  --clean Proteus.py```
  --onefile
  Package your entire application into a single executable file. The default options create a folder of dependencies and executable, whereas --onefile keeps distribution easier by creating only an executable.
7. Once the installation is successful, you have two new folders created called BUILD and DIST, along with a new file with a .spec extension. The .Spec file has the same name as the python script file.PyInstaller creates a distribution directory, DIST containing the main executable and the dynamic libraries bundled in an executable file.
8. Open the Dist Folder to run the Proteus.exe file

## PyInstaller Artifacts
* **A build/ folder**
The build/ folder is where PyInstaller puts most of the metadata and internal bookkeeping for building your executable. The build folder can be useful for debugging
* **A dist/ folder**
The dist/ folder contains the final artifact you’ll want to ship to your users. Inside the dist/ folder, there is a folder named after your entry-point. So in this project, you’ll have a dist/Proteus folder that contains all the dependencies and executable for our application. 
You’ll also find lots of files with the extension .so, .pyd, and .dll depending on your Operating System. These are the shared libraries that represent the dependencies of your project that PyInstaller created and collected.
* __pycache__ folder and .pyc files 
Python is an interpreted language which means that your source code is translated into a set of instructions that can be understood by CPUs at run-time. When running your Python program, the source code is compiled into bytecode which is an implementation detail of CPython. The bytecode is also cached and stored in .pyc files so that the next time you re-run the code the execution of the same file will be faster.

## .Exe limitations
Pyinstaller is not a cross-compiler, which means it can’t create 
binaries for macOS or Linux from Windows and vice versa. You have to run pyinstaller on each platform that you want to support. E.g., if you want to release your software for both Windows and macOS, you’ll have to build the Windows file on Windows and the macOS file on a macOS machine.
Although sharing your code with someone else, using the same OS will work flawlessly most of the time, your mileage may vary when you are on different versions of an OS.

## Reference  
[PyInstaller Documentation](https://pyinstaller.org/en/stable/usage.html).

## License
Distributed under the Open Goverment License. See [LICENSE.txt](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/ for more information.

## Contributing
If you have a suggestion that would make this better, pleace contact:
maria.diapouli@ofwat.gov.uk 
alex.whitmarsh@gov.uk
