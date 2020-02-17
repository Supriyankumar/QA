from selenium import webdriver

class BrowserInteractions():

      def test(self):
          baseUrl = "https://learn.letskodeit.com/p/practice"
          driver = webdriver.Chrome()

          # Maximize the window
          driver.maximize_window()

          # Open the url

          driver.get(baseUrl)

          # get the title
          title = driver.title

          print("Title of the page " + title)

          # Get the current URL
          currentURL = driver.current_url

          print("The current url of the webpage is " + currentURL)

          # Browser refresh

          driver.refresh()

          print ("The browser refreshed once")

          driver.get(currentURL)

          print("The browser refresehes again")

          # open another URL

          driver.get("https://learn.letskodeit.com/p/python-3-from-scratch")

          # current url

          currentURL = driver.current_url
          print("The new url is " + currentURL)

          # Browser back
          driver.back()
          print("Go one step back")

          currentURL = driver.current_url
          print("the previous page was" + currentURL)

          # Browser forward

          driver.forward()
          print("The page goes one step forward")

          currentURL = driver.current_url

          print("forwarded url is now:" + currentURL)

          #get pagesource

          pagesource = driver.page_source
          print(pagesource)
          print("The End =-)")

          # Browser close/quit

         # driver.close()
          driver.quit()

browser1 = BrowserInteractions()
browser1.test()
