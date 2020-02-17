from selenium import webdriver
from selenium.webdriver.common.by import By
class RunTestsOnChrome():

    def test(self):
        baseUrl = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Chrome()
        driver.get(baseUrl)
        elementByID = driver.find_element_by_id('name')
        if elementByID is not None:
           print("ID found")
        elementByName = driver.find_element_by_name('enter-name')
        if elementByName is not None:
            print("Name found")

chromeTest = RunTestsOnChrome()
chromeTest.test()

