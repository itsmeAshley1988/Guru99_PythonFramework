import pytest
from allure_commons.types import AttachmentType
from pageObjects.LoginPage import LoginPage
from Utilities.readProperties import ReadConfig
# from Utilities.customLogger import LogGen
import allure

# @allure.severity(allure.severity_level.NORMAL)
class Test_001_Login:
    baseUrl = ReadConfig.getApplicationURL()
    username_login = ReadConfig.getUsernameLogin()
    password_login = ReadConfig.getPasswordLogin()
    # logger = LogGen.Loggen()

    ##### Login to NewTours App ###########

    # Completed

    @pytest.mark.regression
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_to_newtourspage(self, setup) -> None:
        # self.logger.info("********Login Test********")
        # self.logger.info("********Verification of Login Test*******")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.Click_SignOn_Link()
        self.lp.Insert_Username_field(self.username_login)
        self.lp.Insert_Password_field(self.password_login)
        self.lp.Click_Submit_Button()
        login_confirmation = self.driver.find_element_by_xpath(self.Login_successful_Message).text
        if login_confirmation == "Login Successfully":
            allure.attach(self.driver.get_screenshot_as_png(), name="login", attachment_type=AttachmentType.PNG)
