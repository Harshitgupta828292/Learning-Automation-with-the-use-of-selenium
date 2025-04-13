
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
browser=webdriver.Firefox()
browser.maximize_window()
url="https://the-internet.herokuapp.com/javascript_alerts"
browser.get(url)

# AlertButton=browser.find_element(By.XPATH,value="//button[normalize-space()='Click for JS Confirm']")
AlertButton=browser.find_element(By.XPATH,value="//button[normalize-space()='Click for JS Prompt']")

AlertButton.click()
alert=browser.switch_to.alert
alert_text=alert.text
print(alert_text)
time.sleep(5)
alert.send_keys("this is selenium with python tutorial handling the alert")
# alert.dismiss()
alert.accept()
time.sleep(5)
