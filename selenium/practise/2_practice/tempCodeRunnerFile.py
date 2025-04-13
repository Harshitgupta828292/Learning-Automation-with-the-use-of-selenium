
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
browser=webdriver.Firefox()
browser.maximize_window()
browser.get("https://the-internet.herokuapp.com/iframe")
iframe=browser.find_element(By.ID,value="mce_0_ifr")
browser.switch_to.frame(iframe)

Text_Editor=browser.find_element(By.ID,value="tinymce")
Text_Editor.clear()
Text_Editor.send_keys("this is selenium with python iframe tutorial")
time.sleep(10)