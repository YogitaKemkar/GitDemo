import pytest
from select import select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        log.info("First name is" +getData["firstname"])
        homepage.getName().send_keys(getData["firstname"])
        homepage.getEmail().send_keys(getData["lastname"])
        homepage.getPassword().send_keys("123456")
        homepage.getCheckBox().click()
        self.selectOptionByTest(homepage.getGender(), getData["gender"])
        homepage.submitForm().click()
        message = homepage.alertText().text
        print(message)
        assert "Success" in message
        self.driver.refresh()

        """driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("Hello")
        driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()"""

    @pytest.fixture(params= HomePageData.getTestData("Testcase2"))
    def getData(self, request):
        return request.param
