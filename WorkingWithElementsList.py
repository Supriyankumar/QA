from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class WorkingWithElementsList():
    def test(self):
        baseURL = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(10)

        radioButtonsList = driver.find_elements(By.XPATH,"//input[contains(@type,'radio') and contains(@name,'cars')]")
        size = len(radioButtonsList)
        print("The size of the list:" + str(size))

        for radio in radioButtonsList:
            isSelected = radio.is_selected()
            if not isSelected:
                radio.click()
                time.sleep(2)
l1 = WorkingWithElementsList()
l1.test()





