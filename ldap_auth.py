#!/usr/bin/env python3

# The selenium module
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


if __name__ == '__main__':

	driver = webdriver.Chrome();

	driver.get("http://stgw.iitmandi.ac.in/ug/login.php") # load the web page

	WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.ID, "content"))) # waits till the element with the specific id appears

	absolute_path = resource_path("credentials.txt")

	fo = open(absolute_path, "r")
	username = fo.readline()
	username = username[:-1]
	password = fo.readline()
	elem = driver.find_element_by_name("username") # Find the email input field of the login form
	elem.send_keys(username) # Send the users email
	elem = driver.find_element_by_name("password") # Find the password field of the login form
	elem.send_keys(password) # send the users password
	WebDriverWait(driver, 50) 
	elem.send_keys(Keys.RETURN) # press the enter key
	WebDriverWait(driver, 50) # wait for it to load
	driver.get("http://stgw.iitmandi.ac.in/ug/login_accepted.php") # load the acceptance web page
	driver.close() # closes the driver