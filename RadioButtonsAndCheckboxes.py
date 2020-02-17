from selenium import webdriver
import time

class RadioButtonsAndCheckboxes():
    def test(self):
        baseURL = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(10)

        bmwRadioBtn = driver.find_element_by_id("bmwradio")
        bmwRadioBtn.click()

        time.sleep(2)

        benzRadioBtn = driver.find_element_by_id("benzradio")
        benzRadioBtn.click()

        time.sleep(2)

        bmwCheckbox = driver.find_element_by_id("bmwcheck")
        bmwCheckbox.click()

        time.sleep(2)

        benzCheckbox = driver.find_element_by_id("benzcheck")
        benzCheckbox.click()

        time.sleep(2)

        print("BMW radio button is selected?" + str(bmwRadioBtn.is_selected()))
        print("Benz radio button is selected?" + str(benzRadioBtn.is_selected()))
        print("BMW check button is selected?" + str(bmwCheckbox.is_selected()))
        print("Benz check button is selected?" + str(benzCheckbox.is_selected()))

RC1 = RadioButtonsAndCheckboxes()
RC1.test()
