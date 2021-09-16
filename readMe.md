#Selenium Automation with Python
This document will explain in detail how to setup the Project from scratch up to execution

##Software Requirements for this Framework:

1. Python 
2. Pycharm
3. jdk(1.8 up)

##Plugins to be installed
On Pycharm Navigate to file>Settings> Expand Project name> Python interpreter click + icon and install following plugins:

1. Selenium
2. Pytest
3. Pytest-html
4. allure
5. allure-pytest
6. allure-python-commons

##Framework Project Structure
Packages and folders will be explained

1. The main folder - This is your main folder which consist of the Project Name
2. Configurations -  This folder consist of your .ini file which have your registration, login, flight and common details in it.
3. Reports - This folder consist of your tests reports.
4. PageObjects - This folder consist of all your Page Objects(Models)
5. Test Case - This folder consist of your Test cases
6. Utilities - This folder consist of the readProperties and Log files

##Execution
You can execute the test in two ways:
1. Via windows
2. Via the built-in Terminal in Pycharm

1.1 Via Windows:
Go to the Project folders - double click on the "Run Projcet file" this will launch the command and execute your tests

2.1 Via the built-in Terminal in Pycharm
Open the terminal in Pycharm and enter either of these commands:

pytest -s -v -m"regression" --alluredir="Reports" --browser chrome
pytest -s -v -m"sanity" --alluredir="Reports" --browser chrome

NOTE: To run regression test ensure @pytest.mark.sanity is not in your code or commented out
      To run sanity test ensure @pytest.mark.regression is not in your code or commented out

