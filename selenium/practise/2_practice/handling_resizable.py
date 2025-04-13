from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
browser=webdriver.Firefox()
browser.maximize_window()
browser.get("https://demo.automationtesting.in/Resizable.html")
resizeable_element=browser.find_element(By.XPATH,value="//div[@class='ui-resizable-handle ui-resizable-se ui-icon ui-icon-gripsmall-diagonal-se']")
Initial_element_size=browser.find_element(By.XPATH,value="//div[@id='resizable']")
initial_size=Initial_element_size.size
print("Initial Size",initial_size)
time.sleep(3)
action_chains=ActionChains(browser)
action_chains.click_and_hold(resizeable_element).move_by_offset(xoffset=100,yoffset=100).release().perform()
time.sleep(3)
resized_element=Initial_element_size.size
print("resized element",resized_element)
browser.quit()
