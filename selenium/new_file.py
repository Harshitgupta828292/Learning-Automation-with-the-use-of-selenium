from selenium import webdriver
from selenium .webdriver.common.by import By
# import time


driver= webdriver.Firefox()
driver.get('http://selenium.dev/')
# time.sleep(5)
# for maximum window we use 
driver.maximize_window()
# browser.get('http://google.dev/')
# time.sleep(4)
title=driver.title
print(title)
# assert "Selenium123" in title
assert "Selenium" in title
driver.find_element(By.XPATH,("#APjFqb"))
                    #  ELEMENTS-checkboxes,links,text field
                    # LOCATOR-ID,name,classname,css selector,xpath,linktext,partial link text,tag name
                    # INTERACTION -text field, typing something, checkbox-checking the box,link-clicking the link
                    # ASSERTION-verify the functionality,verify there should be a button with a text login