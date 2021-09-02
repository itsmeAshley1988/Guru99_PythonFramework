from selenium import webdriver
import pytest
from selenium.webdriver import  DesiredCapabilities
from selenium.webdriver.chrome.options import Options

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path=".\Drivers\chromedriver.exe")
        print("Launching chrome browser")
    elif browser == 'firefox':
        driver = webdriver.Firefox(
            executable_path=""
        )
        print("Launching firefox browser")
    else:
        driver = webdriver.Ie(
            executable_path=""
        )
        print("Launching IE browser")
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

###### pytest HTML report ######

# hooks for adding environment info to HTML report
def pytest_configure(config):
    config._metadata['Project Name'] = 'NewTours - Guru 99 Python'
    config._metadata['Module Name'] = 'POC'
    config._metadata['Tester Name'] = 'Ashley'

# hooks
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
   # metadata.pop("JAVA_HOME", None)
  #  metadata.pop("Plugin", None)
