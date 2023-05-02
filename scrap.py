
from selenium_driver import  SeleniumDriver
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
'''
list of websites to scrap:
main_box_class = "Box-sc-g0xbh4-0 iQZHd code-list"
box_header_class = "Box-sc-g0xbh4-0 kyCKqA"
'''

class Scrap(SeleniumDriver):

    def __init__(self,ip=""):

        SeleniumDriver.__init__(self, remote_ip_addr= ip)
    
    def login(self):
        # Create a new instance of the Firefox driver
        self.open_driver("https://github.com/login")
        self.driver.implicitly_wait(10)
        # Find the username and password fields, and enter your login credentials
        username_field = self.driver.find_element(By.CSS_SELECTOR ,"#login_field")
        username_field.send_keys(os.environ.get("username", "doe"))
        password_field = self.driver.find_element(By.CSS_SELECTOR ,"#password")
        password_field.send_keys(os.environ.get("password", "nop"))
        password_field.send_keys(Keys.RETURN)
        self.driver.implicitly_wait(3)
        passcode = input("Enter passcode!")
        passcode_field= self.driver.find_element(By.CSS_SELECTOR, "#sms_totp")
        passcode_field.send_keys(passcode)

        # Wait for the login process to complete
        self.driver.implicitly_wait(10)

        #show the screen
        self.driver.get_screenshot_as_file("view.png")

        # # Verify that we are logged in by checking the presence of search field
        try:
            self.driver.find_element(By.CSS_SELECTOR,"#query-builder-test")
            print("Login successful!")
        except:
            print("Login failed.")

         # go to abap search page
        self.open_driver("https://github.com/search?q=abap+language%3AABAP&type=code")
        self.driver.implicitly_wait(10)

        # show current screen
        self.driver.get_screenshot_as_file("abap_codes.png")

        # Close the browser
        self.close_driver()


    def main_box(self, url):
        """_summary_
        """
        self.open_driver(url)
        xpath = self.get_all_xpath()
        #self.find_element_by_class_name(main_box_class)
        #container_elems = self.find_element_by_class_name()
        print(xpath)
        self.close_driver()

if __name__=="__main__":
    ip = os.environ.get("ip", "localhost")
    scrap = Scrap(ip= ip)
    scrap.login()
    url ="https://github.com/search?q=abap+language%3AABAP&type=code"
