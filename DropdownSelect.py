from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

class DropDownSelect():
    def test(self):
        baseURL = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseURL)

        driver.implicitly_wait(10)

        element = driver.find_element_by_id("carselect")
        sel = Select(element)
        sel.select_by_value("benz")
        print("Select benz value")
        time.sleep(2)

        sel.select_by_index("2")
        print("Select Honda by index")
        time.sleep(2)

        sel.select_by_visible_text("BMW")
        print("Select BMW by visible text")
        time.sleep(2)

        sel.select_by_index(2)
        print("Select Honda by index")
drop1 = DropDownSelect()
drop1.test()

