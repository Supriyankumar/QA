from selenium import webdriver
import time

class HiddenElements():

    def test(self):

        baseURL = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(2)

        # find the state of the text box
        textBoxElement = driver.find_element_by_id("displayed-text")
        textBoxState = textBoxElement.is_displayed() # True if visible and False if hidden
        # exception if not present  in the DOM
        print("Text is visible?" + str(textBoxState))
        time.sleep(2)
        #Click the hde button

        driver.find_element_by_id("hide-textbox").click()

        # find the state of the text box
        textBoxElement = driver.find_element_by_id("displayed-text")
        textBoxState = textBoxElement.is_displayed()  # True if visible and False if hidden
        # exception if not present  in the DOM
        print("Text is visible?" + str(textBoxState))
        time.sleep(2)

        #Click the show button

        driver.find_element_by_id("show-textbox").click()
        # find the state of the text box
        textBoxElement = driver.find_element_by_id("displayed-text")
        textBoxState = textBoxElement.is_displayed()  # True if visible and False if hidden
        # exception if not present  in the DOM
        print("Text is visible?" + str(textBoxState))
        time.sleep(2)

        # browser close

        driver.quit()

    def testExpedia(self):
        baseURL = "https://www.expedia.com"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(3)

        driver.find_element_by_id("tab-flight-tab").click()
        drpdwnElement = driver.find_element_by_id("flight-age-select-1")
        print("element visible" + str(drpdwnElement.is_displayed()))

test1 = HiddenElements()
test1.test()
test1.testExpedia()






