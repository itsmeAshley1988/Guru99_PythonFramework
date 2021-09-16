from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC,wait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select

class RegistrationPage:
    ## All Locators for Registrations ##
    link_Registration_xpath = "//a[@href='register.php'][contains(.,'REGISTER')]"
    input_FirstName_xpath = "//input[contains(@name,'firstName')]"
    input_LastName_xpath = "//input[contains(@name,'lastName')]"
    input_Phone_xpath = "//input[contains(@name,'phone')]"
    input_Email_xpath = "//input[contains(@id,'userName')]"
    input_Address_xpath = "//input[contains(@name,'address1')]"
    input_City_xpath = "//input[contains(@name,'city')]"
    input_Province_xpath = "//input[contains(@maxlength,'40')]"
    input_PostalCode_xpath = "//input[contains(@name,'postalCode')]"
    select_CountryName_xpath = "//select[contains(@name,'country')]"
    input_Username_xpath = "//input[contains(@name,'email')]"
    input_Password_xpath = "//input[contains(@name,'password')]"
    input_ConfirmPassword_xpath = "//input[contains(@name,'confirmPassword')]"
    button_SubmitButton_xpath = "//input[contains(@name,'submit')]"
    label_SuccessfulRegistration_xpath = "//b[contains(.,'Note: Your user name is Ashley.')]"
    link_SignInLink_after_SuccessfulReg_xpath = "//a[@href='login.php'][contains(.,'sign-in')]"

    def __init__(self, driver):
        self.driver = driver

    def clickRegisterLink(self):
        wait = WebDriverWait(self.driver, 30)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.link_Registration_xpath)))
        element.click()

    def insert_Name_field(self, firstName):
        element = self.driver.find_element_by_xpath(self.input_FirstName_xpath)
        element.send_keys(firstName)

    def insert_LastName_field(self, lastName):
        element = self.driver.find_element_by_xpath(self.input_LastName_xpath)
        element.send_keys(lastName)

    def insert_Phone_field(self, phone):
        element = self.driver.find_element_by_xpath(self.input_Phone_xpath)
        element.send_keys(phone)

    def insert_Email_field(self, email):
        element = self.driver.find_element_by_xpath(self.input_Email_xpath)
        element.send_keys(email)

    def insert_Address_field(self, address):
        element = self.driver.find_element_by_xpath(self.input_Address_xpath)
        element.send_keys(address)

    def insert_City_field(self, city):
        element = self.driver.find_element_by_xpath(self.input_City_xpath)
        element.send_keys(city)

    def insert_Province_field(self, province):
        element = self.driver.find_element_by_xpath(self.input_Province_xpath)
        element.send_keys(province)

    def insert_PostalCode_field(self, postal_code):
        element = self.driver.find_element_by_xpath(self.input_PostalCode_xpath)
        element.send_keys(postal_code)

    def select_Country_dropdown(self, country):
        dropdown = Select(self.driver.find_element_by_xpath(self.select_CountryName_xpath))
        dropdown.select_by_value(country)

    def insert_UserName_field(self, username):
        element = self.driver.find_element_by_xpath(self.input_Username_xpath)
        element.send_keys(username)

    def insert_Password_field(self, password):
        element = self.driver.find_element_by_xpath(self.input_Password_xpath)
        element.send_keys(password)

    def insert_ConfirmPassword_field(self, confirm_password):
        element = self.driver.find_element_by_xpath(self.input_ConfirmPassword_xpath)
        element.send_keys(confirm_password)

    def click_SubmitButton(self):
        element = self.driver.find_element_by_xpath(self.button_SubmitButton_xpath)
        element.click()

    def click_SignIn_AfterReg(self):
        wait = WebDriverWait(self.driver, 30)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.link_SignInLink_after_SuccessfulReg_xpath)))
        element.click()




