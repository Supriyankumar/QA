from selenium import webdriver
import time
from selenium.webdriver.common.by import By

class GetText():
    def test(self):
        baseURL = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(baseURL)

        openTabElement = driver.find_element(By.ID,"opentab")
        elementText = openTabElement.text
        print("Text on element is: " + elementText)
        time.sleep(1)
        driver.quit()


gettext1 = GetText()
gettext1.test()
