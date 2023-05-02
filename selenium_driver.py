
#selenium driver
#import chromedriver_binary
from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from driver import  get_driver



class SeleniumDriver():

    def __init__(self, remote_ip_addr) -> None:

        self.remote_ip_addr = remote_ip_addr
        self.driver = get_driver(self.remote_ip_addr)

    def open_driver(self, url:str):
        """
        Args:
           url: str
        Returns:
            open the selenium driver
        """
        self.driver.get(url)

    def close_driver(self):
        """
        Args:
        
        Returns:
            close the Selenium driver
        """ 
        self.driver.quit()



    def get_all_xpath(self):
        """
        Args:
         
        Returns:
            xpath_element: 
        """
        return self.driver.find_elements(By.XPATH ,".//*" )



    def search_body(self, empty_body_element_class_name = "pf-c-empty-state__body"):

        element_body = ''
      
        try:
            element_body = WebDriverWait(self.driver,8).until(EC.presence_of_element_located((By.CLASS_NAME, empty_body_element_class_name ))).text
        
        finally:
            return element_body


    def find_element_by_css_selector(self, selector:str):

        elements = None
        try: 
            elements = self.driver.find_element(By.CSS_SELECTOR , selector)
        except Exception as e: 
            print(e)
        return  elements


    def find_element_by_class_name(self, class_name:str):
        """
        Args:
    
        Returns:
            elements containing search results
        """

        elements = None

  
        try:
            elements = WebDriverWait(self.driver, 3).until(
        EC.presence_of_element_located((By.CLASS_NAME, class_name))
    )   
        except Exception as e:
            print("error.  {}".format(e))
        
        return  elements
      

    