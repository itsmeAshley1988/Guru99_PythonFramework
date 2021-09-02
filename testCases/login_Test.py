import pytest
from allure_commons.types import AttachmentType
from pageObjects.loginPage import LoginPage
from utilities.readProperties import ReadConfig
# from utilities.customLogger import LogGen
import allure

@allure.severity(allure.severity_level.NORMAL)
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
        self.lp.clickSignOnLink()
        self.lp.insertUsernamefield(self.username_login)
        self.lp.insertPasswordfield(self.password_login)
        self.lp.clickSubmitButton()
        login_confirmation = self.driver.find_element_by_xpath(self.lp.login_successful_Message).text
        if login_confirmation == "Login Successfully":
           allure.attach(self.driver.get_screenshot_as_png(), name="login",
                         attachment_type=AttachmentType.PNG)
           # self.logger.error("**************Verification Login Passed***************")
           self.driver.close()
           assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="login",
                          attachment_type=AttachmentType.PNG)
          #  self.logger.critical("***************Verification of Login Test Failed**************")
            self.driver.close()
            assert False

