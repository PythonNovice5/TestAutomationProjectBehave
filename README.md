# TestAutomationProjectBehave

**Prerequisites** - 
1. google chrome version 92.X installed in the system
2. 'git' installed
3. Python 3.x installed (in Linux it comes by default as preinstalled). For Windows it can be downloaded and installed from: https://www.python.org/downloads/

---------------------------------------------------------------------------------------
                                        LINUX
---------------------------------------------------------------------------------------

**Instructions to run the test cases on Linux**

1. git clone https://github.com/PythonNovice5/TestAutomationProjectBehave
2. cd TestAutomationProjectBehave
3. chmod 755 Drivers/unix/chromedriver
4. sudo apt update -y
5. sudo apt install python3-pip -y
6. sudo apt install python3-behave -y
7. pip3 install selenium


**After all the required dependancies are installed, run the test scenarios using:**

behave -D os=linux --no-capture 


---------------------------------------------------------------------------------------
                                        WINDOWS
---------------------------------------------------------------------------------------

**Instructions to run the test cases on Windows**
Open GIT bash terminal and perform the following:
1. git clone https://github.com/PythonNovice5/TestAutomationProjectBehave
2. cd TestAutomationProjectBehave
3. pip install behave
4. pip install selenium

**After all the required dependancies are installed, run the test scenarios using:**

behave -D os=windows --no-capture


**Important Details:**
1. The test scenarios are validating all the 4 fields for the combination of sort and filter data inputs
2. The code runs on both Windows and Linux on Chrome browser

