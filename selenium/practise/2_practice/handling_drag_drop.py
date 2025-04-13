from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
browser=webdriver.Firefox()
browser.maximize_window()
browser.get("https://the-internet.herokuapp.com/drag_and_drop")
source_element=browser.find_element(By.ID,value="column-a")
desitination_element=browser.find_element(By.ID,value="column-b")
action=ActionChains(browser)
action.drag_and_drop(source_element,desitination_element).perform()
time.sleep(5)
browser.quit()