import pytest
from allure_commons.types import AttachmentType
from pageObjects.loginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import allure

@allure.severity(allure.severity_level.NORMAL)
class Test_002_Login:
    baseUrl = ReadConfig.getApplicationURL()
    username_login = ReadConfig.getUsernameLogin()
    password_login = ReadConfig.getPasswordLogin()
    logger = LogGen.loggen()

    ##### Login to NewTours App ###########

    # Completed

   # @pytest.mark.regression
    @allure.severity(allure.severity_level.BLOCKER)
    def test_login_with_valid_details(self, setup) -> None:
        # Test start here
        self.logger.info("***********************Login with Valid details Test*********************")
        self.logger.info("**********************Verification of Login with valid details Test started********************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.clickSignOnLink()
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
            allure.attach(self.driver.get_screenshot_as_png(), name="test_login_with_valid_details",
                          attachment_type=AttachmentType.PNG)
            self.logger.error("************************Login with Valid details Test has Failed************************")
            self.driver.close()
            assert False

   #  @pytest.mark.regression
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_with_invalid_details(self, setup) -> None:
        # Test start here
        self.logger.info("************************Login with Invalid details Test*********************")
        self.logger.info("**********************Verification of Login with Invalid details Test*****************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.clickSignOnLink()
        self.lp.insertUsernamefield(self.username_login+str("test"))
        self.lp.insertPasswordfield(self.password_login+str("test"))
        self.lp.clickSubmitButton()
        Unsucessful_login_confirmation = self.driver.find_element_by_xpath(self.lp.label_UnsuccessfulLogin_xpath).text
        if Unsucessful_login_confirmation == "Enter your userName and password correct":
           allure.attach(self.driver.get_screenshot_as_png(), name="test_login_with_invalid_details",
                         attachment_type=AttachmentType.PNG)
           self.logger.info("***********************Login with Invalid details Test has Passed*********************")
           self.driver.close()
           assert True

        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="test_login_with_invalid_details",
                          attachment_type=AttachmentType.PNG)
            self.logger.error("************************Login with Invalid details Test has Test Failed*********************")
            self.driver.close()
            assert False



