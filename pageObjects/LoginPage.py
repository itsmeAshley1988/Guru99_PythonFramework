from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait

class LoginPage:
    ##### All Locators for Login ########

    link_SignOn_xpath = "//a[@href='login.php'][contains(.,'SIGN-ON')]"

    input_Username_xpath = "//input[contains(@name,'userName')]"

    input_Password_xpath = "//input[contains(@name,'password')]"

    Submit_Button_xpath = "//input[contains(@type,'submit')]"

    def __init__(self, driver):
        self.driver = driver

    def Click_SignOn_Link(self):
        wait = WebDriverWait(self.driver, 30)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.link_SignOn_xpath)))
        element.click()












