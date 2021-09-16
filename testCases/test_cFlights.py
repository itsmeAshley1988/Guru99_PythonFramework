import pytest
from allure_commons.types import AttachmentType
from pageObjects.loginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.flightsPage import FlightsPage
from selenium import webdriver
import allure

@allure.severity(allure.severity_level.CRITICAL)
class Test_003_Flights:
    baseUrl = ReadConfig.getApplicationURL()
    username_login = ReadConfig.getUsernameLogin()
    password_login = ReadConfig.getPasswordLogin()
    flight_type = ReadConfig.getFlightType()
    passengers = ReadConfig.getPassengerCount()
    departingFrom = ReadConfig.getDepartingFrom()
    departingMonth = ReadConfig.getDepartingMonth()
    departingDay = ReadConfig.getDepartingDay()
    arrivingIn = ReadConfig.getArrivingCountry()
    returningMonth = ReadConfig.getReturningMonth()
    returningDay = ReadConfig.getReturningDay()
    serviceClass = ReadConfig.getServiceClass()
    airline = ReadConfig.getAirlineName()
    logger = LogGen.loggen()

    @pytest.mark.regression
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Verify_user_on_flightsPage(self, setup) -> None:
        self.logger.info("*************Verify user on Flights Page Test************")
        self.logger.info("**************Verification user is on Flights Page Test************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.fp = FlightsPage(self.driver)
        self.lp.clickSignOnLink()
        self.lp.insertUsernamefield(self.username_login)
        self.lp.insertPasswordfield(self.password_login)
        self.lp.clickSubmitButton()
        self.fp.click_flightPage_Link()
        self.fp.select_passengerCount_dropdown(self.passengers)
        self.fp.select_departCountry_dropdown(self.departingFrom)
        self.fp.select_monthDeparting_dropdown(self.departingMonth)
        self.fp.select_dayDeparting_dropdown(self.departingDay)
        self.fp.select_arrivingCountry_dropdown(self.arrivingIn)
        self.fp.select_returningMonth_dropdown(self.returningMonth)
        self.fp.select_returningDay_dropdown(self.returningDay)
        self.fp.select_serviceClass_radioBtn()
        self.fp.select_airline_dropdown(self.airline)
        self.fp.click_continue_button()



        flights_page_confirmation = self.driver.find_element_by_xpath(self.fp.label_successful_flightFinder_xpath).text
        if flights_page_confirmation == '''Please press your browser's back button to return to the previous page or click the "BACK TO HOME" icon below to go to the homepage.''':
            allure.attach(self.driver.get_screenshot_as_png(), name="Verify user on Flights Page",
                          attachment_type=AttachmentType.PNG)
            self.logger.info("*************Login with Valid details and verify user is on Flights Page Test Passed********")

            self.fp.click_home_button()

            self.driver.close()
            assert True

        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Verify user on Flights Page",
                          attachment_type=AttachmentType.PNG)
            self.logger.error("***************Login with Valid details and verify user is on Flights Page Test Failed*******")
            self.driver.close()
            assert False


