from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
browser=webdriver.Firefox()
browser.maximize_window()
url="https://demo.automationtesting.in/Datepicker.html"
browser.get(url)
actions=ActionChains(browser)
hover_element=browser.find_element(By.XPATH,value="//a[normalize-space()='SwitchTo']")
time.sleep(5)
actions.move_to_element(hover_element).perform()
browser.find_element(By.XPATH,value="//a[normalize-space()='Frames']").click()
time.sleep(5)
browser.switch_to.frame(browser.find_element(By.XPATH,"//iframe[@id='singleframe']"))
Write_element=browser.find_element(By.XPATH,value="//input[@type='text']")
Write_element.clear()
Write_element.send_keys("this is the first cycle")
time.sleep(5)
browser.switch_to.default_content()
browser.quit()
# action action is use for mouse button key press
