from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
browser=webdriver.Firefox()
browser.maximize_window()
browser.get('https://the-internet.herokuapp.com/horizontal_slider')
slider=browser.find_element(By.XPATH,value="//input[@type='range']")
actions=ActionChains(browser)
actions.click_and_hold(slider).move_by_offset(xoffset=50,yoffset=0).release().perform()
time.sleep(5)
browser.quit()