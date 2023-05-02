
"""
Module for web scraping
"""
from selenium import webdriver


def get_driver(remote_ip:str):

    print("Waiting for selenium webdriver to load a session...")
    print(remote_ip)
    
    try:
        driver = webdriver.Remote(desired_capabilities=webdriver.DesiredCapabilities.CHROME, command_executor="http://{}:4444".format(remote_ip))
    except Exception as e: 
        print("error: {}".format(e))
        exit()

    return driver

    

