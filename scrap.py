
from selenium_driver import  SeleniumDriver
import os
from selenium.webdriver.common.keys import Keys
import json

class Scrap(SeleniumDriver):

    def __init__(self,ip=""):
        SeleniumDriver.__init__(self, remote_ip_addr= ip)
    
    def search_element(self,element_type: str , element: str):
        """_summary_

        Args:
            element_type (str): _description_
        """
        if element_type == "xpath":
            return self.find_element_by_xpath(element)
        elif element_type =="class":
            return self.find_element_by_class_name(element)
        elif element_type =="selector":
            return self.find_element_by_css_selector(element)
        else: 
            print("no valid element_type")
        
    def take_screenshot(self, filename="photo"):
        """
        
        """
        self.driver.get_screenshot_as_file(filename)
        
    def repositories(self):
        """
        
        """
        repo_names = []
       
        for page in list(range(100)):
            print("page: ",page+1)
            repositories= "https://github.com/search?q=abap+language%3AABAP&type=repositories&p={}".format(page+1)
            self.open_driver(repositories)
            self.driver.implicitly_wait(3)
            for index in list(range(10)):
                
                xpath = "/html/body/div[1]/div[6]/main/react-app/div/div/div/div[1]/div/div/main/div[2]/div/div/div[4]/div/div/div[{}]".format(index+1)
                elements =self.search_element("xpath", xpath) 
                
                if elements is not None:
                    name = elements.text.split("\n")[0]
                    print(name)
                    
                    repo_names.append(name)
        with open("repos.json", "w", encoding="utf-8") as rep:
            rep.write(json.dumps(repo_names , indent=4))

    
    def login(self):
        
        # Create a new instance of the Firefox driver
        self.open_driver("https://github.com/login")
        self.driver.implicitly_wait(3)
        
        # Find the username and password fields, and enter your login credentials
        username_field = self.search_element("selector", "#login_field") 
        username_field.send_keys(os.environ.get("username","nope"))
        password_field = self.search_element("selector","#password" )
        password_field.send_keys(os.environ.get("password","pass"))
        password_field.send_keys(Keys.RETURN)
        self.driver.implicitly_wait(3)
        passcode = input("Enter passcode!")
        
        passcode_field= self.search_element("selector","#sms_totp") 
        passcode_field.send_keys(passcode)
        # Wait for the login process to complete
        self.driver.implicitly_wait(3)
       
        self.take_screenshot("github.png")

        # # Verify that we are logged in by checking the presence of search field
        try:
            self.search_element("selector", "#query-builder-test")
            print("Login successful!")
        except  Exception as e:
            print("Login failed. Raised: {}".format(e))

     


if __name__=="__main__":
    ip = os.environ.get("ip", "172.17.0.3")
    scrap = Scrap(ip= ip)
    scrap.login()
    scrap.repositories()
  
