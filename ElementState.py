from selenium import webdriver

class ElementState():

    def test(self):

        baseURL = "http://www.google.com"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(3)

        e1 = driver.find_element_by_id("gs_htif0")
        e1State = e1.is_enabled()

        # true for enabled and false for disabled

        print("E1 is Enabled? -> " + str(e1State))

        e2 = driver.find_element_by_id("gs_taif0")
        e2State = e2.is_enabled()
        print("E2 is Enabled? -> " + str(e2State))

        e3 = driver.find_element_by_id("lst-ib")
        e3State = e1.is_enabled()
        print("E3 is Enabled? -> " + str(e3State))

        e3.send_keys("letskodeit")

state1 = ElementState()
state1.test()