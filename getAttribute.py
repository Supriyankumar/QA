from selenium import webdriver
import time

class getAttribute():

    def test(self):
        baseURL = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(baseURL)

        element = driver.find_element_by_id("name")
        result = element.get_attribute("placeholder")

        print("Value of attribute is " + result)
        time.sleep(1)

        driver.quit()

attr = getAttribute()
attr.test()

