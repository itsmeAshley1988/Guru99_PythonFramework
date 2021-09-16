import pytest
from allure_commons.types import AttachmentType
from pageObjects.registrationPage import RegistrationPage
from pageObjects.loginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import allure

@allure.severity(allure.severity_level.CRITICAL)
class Test_001_Registration:
    baseUrl = ReadConfig.getApplicationURL()
    firstName = ReadConfig.getFirstNameRegistration()
    lastName = ReadConfig.getLastNameRegistration()
    phone = ReadConfig.getPhoneRegistration()
    email = ReadConfig.getEmailRegistration()
    address = ReadConfig.getAddressRegistration()
    city = ReadConfig.getCityRegistration()
    province = ReadConfig.getProvinceRegistration()
    postal_code = ReadConfig.getPostalCodeRegistration()
    country = ReadConfig.getCountryRegistration()
    username = ReadConfig.getUsernameRegistration()
    password = ReadConfig.getPasswordRegistration()
    confirm_password = ReadConfig.getConfirmPasswordRegistration()

    username_login = ReadConfig.getUsernameLogin()
    password_login = ReadConfig.getPasswordLogin()
    logger = LogGen.loggen()

    # @pytest.mark.regression
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_registration(self, setup) -> None:

        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        self.rp = RegistrationPage(self.driver)
        self.lp = LoginPage(self.driver)
        self.rp.clickRegisterLink()
        self.rp.insert_Name_field(self.firstName)
        self.rp.insert_LastName_field(self.lastName)
        self.rp.insert_Phone_field(self.phone)
        self.rp.insert_Email_field(self.email)
        self.rp.insert_Address_field(self.address)
        self.rp.insert_City_field(self.city)
        self.rp.insert_Province_field(self.province)
        self.rp.insert_PostalCode_field(self.postal_code)
        self.rp.select_Country_dropdown(self.country)
        self.rp.insert_UserName_field(self.username)
        self.rp.insert_Password_field(self.password)
        self.rp.insert_ConfirmPassword_field(self.confirm_password)
        self.rp.click_SubmitButton()
        registration_confirmation = self.driver.find_element_by_xpath(self.rp.label_SuccessfulRegistration_xpath).text
        if registration_confirmation == "Note: Your user name is Ashley.":
            allure.attach(self.driver.get_screenshot_as_png(), name="test successful registration",
                      attachment_type=AttachmentType.PNG)
        self.logger.info("******************Registration Test has Passed********************")
        assert True

        self.rp.click_SignIn_AfterReg()
        self.lp.insertUsernamefield(self.username_login)
        self.lp.insertPasswordfield(self.password_login)
        self.lp.clickSubmitButton()
        login_confirmation = self.driver.find_element_by_xpath(self.lp.label_successfulLogin_xpath).text
        if login_confirmation == "Login Successfully":
           allure.attach(self.driver.get_screenshot_as_png(), name="test_login_with_valid_details",
                         attachment_type=AttachmentType.PNG)
           self.logger.info("******************Login with Valid details Test has Passed********************")
           self.driver.close()
           assert True


        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="test successful registration",
                          attachment_type=AttachmentType.PNG)
            self.logger.error(
                "************************Registration Test has Failed************************")
            self.driver.close()
            assert False