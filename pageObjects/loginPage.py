from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC,wait
from selenium.webdriver.support.wait import WebDriverWait




class LoginPage:
    ##### All Locators for Login ########

    link_SignOn_xpath = "//a[@href='login.php'][contains(.,'SIGN-ON')]"
    input_Username_xpath = "//input[@name='userName']"
    input_Password_xpath = "//input[@name='password']"
    submit_Button_xpath = "//input[@name='submit']"
    label_successfulLogin_xpath = "//h3[contains(.,'Login Successfully')]"
    label_UnsuccessfulLogin_xpath = "//span[contains(.,'Enter your userName and password correct')]"

    def __init__(self, driver):
        self.driver = driver

    def clickSignOnLink(self):
        wait = WebDriverWait(self.driver, 30)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.link_SignOn_xpath)))
        element.click()

    def insertUsernamefield(self, username_login):
        wait = WebDriverWait(self.driver, 30)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.input_Username_xpath)))
        element.send_keys(username_login)

    def insertPasswordfield(self, password_login):
        wait = WebDriverWait(self.driver, 30)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.input_Password_xpath)))
        element.send_keys(password_login)

    def clickSubmitButton(self):
        wait = WebDriverWait(self.driver, 30)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.submit_Button_xpath)))
        element.click()














