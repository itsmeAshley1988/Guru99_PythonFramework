from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC,wait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium import webdriver

class FlightsPage:

    link_flightsPage_xpath = "//a[@href='reservation.php'][contains(.,'Flights')]"
    radio_button_tripType_xpath = "//input[@value='roundtrip']"
    drp_down_passengerCount_xpath = "//select[contains(@name,'passCount')]"
    drp_down_departingCountry_xpath = "//select[contains(@name,'fromPort')]"
    drp_down_monthDeparting_xpath = "//select[contains(@name,'fromMonth')]"
    drp_down_dayDeparting_xpath = "//select[@name='fromDay']"
    drp_down_arrivingCountry_xpath = "//select[contains(@name,'toPort')]"
    drp_down_monthReturning_xpath = "//select[contains(@name,'toMonth')]"
    drp_down_dayReturning_xpath = "//select[contains(@name,'toDay')]"
    radio_button_classType_xpath = "//input[@value='Business']"
    drp_down_airlineName_xpath = "//select[contains(@name,'airline')]"
    button_continueButton_xpath = "//input[contains(@name,'findFlights')]"
    label_successful_flightFinder_xpath = "(//font[contains(@size,'3')])[3]"
    button_homeButton_xpath = "//img[@src='images/home.gif']"


    def __init__(self, driver):
        self.driver = driver

    def click_flightPage_Link(self):
            wait = WebDriverWait(self.driver, 30)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, self.link_flightsPage_xpath)))
            element.click()

    def select_tripType_radioBtn(self):
        radioBtn1 = self.driver.find_element_by_xpath(self.radio_button_tripType_xpath)
        radioBtn1.click()

    def select_passengerCount_dropdown(self, passengers):
        dropdown = Select(self.driver.find_element_by_xpath(self.drp_down_passengerCount_xpath))
        dropdown.select_by_value(passengers)

    def select_departCountry_dropdown(self, departingFrom):
        dropdown = Select(self.driver.find_element_by_xpath(self.drp_down_departingCountry_xpath))
        dropdown.select_by_value(departingFrom)

    def select_monthDeparting_dropdown(self, departingMonth):
        dropdown = Select(self.driver.find_element_by_xpath(self.drp_down_monthDeparting_xpath))
        dropdown.select_by_visible_text(departingMonth)

    def select_dayDeparting_dropdown(self, departingDay):
        dropdown = Select(self.driver.find_element_by_xpath(self.drp_down_dayDeparting_xpath))
        dropdown.select_by_value(departingDay)

    def select_arrivingCountry_dropdown(self, arrivingIn):
        dropdown = Select(self.driver.find_element_by_xpath(self.drp_down_arrivingCountry_xpath))
        dropdown.select_by_value(arrivingIn)

    def select_returningMonth_dropdown(self, returningMonth):
        dropdown = Select(self.driver.find_element_by_xpath(self.drp_down_monthReturning_xpath))
        dropdown.select_by_visible_text(returningMonth)

    def select_returningDay_dropdown(self, returningDay):
        dropdown = Select(self.driver.find_element_by_xpath(self.drp_down_dayReturning_xpath))
        dropdown.select_by_value(returningDay)

    def select_serviceClass_radioBtn(self):
        radioBtn1 = self.driver.find_element_by_xpath(self.radio_button_classType_xpath)
        radioBtn1.click()

    def select_airline_dropdown(self, airline):
        dropdown = Select(self.driver.find_element_by_xpath(self.drp_down_airlineName_xpath))
        dropdown.select_by_visible_text(airline)

    def click_continue_button(self):
        wait = WebDriverWait(self.driver, 30)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.button_continueButton_xpath)))
        element.click()

    def click_home_button(self):
        wait = WebDriverWait(self.driver, 30)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.button_homeButton_xpath)))
        element.click()

