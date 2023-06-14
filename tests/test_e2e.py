import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        checkOutPage = homePage.shopItems()
        log.info("getting all the card titles")
        products = checkOutPage.getCardTitles()

        for product in products:
            productName = product.find_element(By.XPATH, "div/h4/a").text
            if productName == 'Blackberry':
                checkOutPage.getCardFooter()

        self.driver.find_element(By.CSS_SELECTOR, "a[class*='nav-link btn btn-primary']").click()
        #time.sleep(2)

        confirmPage = checkOutPage.checkOutItems()
        log.info("Enter country name as ind")
        self.driver.find_element(By.ID, "country").send_keys("Ind")
        self.verifyLinkPresence("India")
        linkIn = checkOutPage.linkIndia()
        checkIt = checkOutPage.checked()
        #time.sleep(2)
        submit = checkOutPage.submitBtn()
        time.sleep(2)

        successTxt = self.driver.find_element(By.CLASS_NAME, "alert").text
        log.info("Text received from application is" +successTxt)

        assert "Success! Thank you" in successTxt




