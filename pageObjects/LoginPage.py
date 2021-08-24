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

    Login_successful_Message = "//h3[contains(.,'Login Successfully')]"

    def __init__(self, driver):
        self.driver = driver

    def Click_SignOn_Link(self):
        wait = WebDriverWait(self.driver, 30)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.link_SignOn_xpath)))
        element.click()

    def Insert_Username_field(self, username_login):
        element = (EC.element_to_be_clickable((By.XPATH, self.input_Username_xpath)))
        element.send_keys(username_login)

    def Insert_Password_field(self, password_login):
        element = (EC.element_to_be_clickable((By.XPATH, self.input_Password_xpath)))
        element.send_keys(password_login)

    def Click_Submit_Button(self, submit_button):
        element = (EC.element_to_be_clickable((By.XPATH, self.Submit_Button_xpath)))
        element.send_keys(submit_button)

    def Login_Verification(self, login_successfully):
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.Login_successful_Message)))
        element.click()













