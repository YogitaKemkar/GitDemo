from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    cardTitle = (By.XPATH, "//div[@class='card h-100']")
    cardFooter = (By.XPATH, "div/button")
    checkOut = (By.XPATH, "//button[@class='btn btn-success']")
    linkInd = (By.LINK_TEXT, "India")
    checkBox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    submitButton = (By.XPATH, "//input[@type='submit']")

    def getCardTitles(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle)

    def getCardFooter(self):
        return self.driver.find_elements(*CheckOutPage.cardFooter)

    def checkOutItems(self):
        self.driver.find_element(*CheckOutPage.checkOut).click()
        confirmPage = ConfirmPage()
        return confirmPage

    def linkIndia(self):
        self.driver.find_element(*CheckOutPage.linkInd).click()
        linkIn = CheckOutPage(self.driver)
        return linkIn

    def checked(self):
        self.driver.find_element(*CheckOutPage.checkBox).click()
        checkIt = CheckOutPage(self.driver)
        return checkIt

    def submitBtn(self):
        self.driver.find_element(*CheckOutPage.submitButton).click()
        submit = CheckOutPage(self.driver)
        return submit





