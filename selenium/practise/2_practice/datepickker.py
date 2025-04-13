from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import Keys
from datetime import datetime, timedelta
browser=webdriver.Firefox()
browser.maximize_window()
url="https://www.globalsqa.com/demo-site/datepicker/"
browser.get(url)
browser.find_element(By.XPATH,value="//div[@class='single_tab_div resp-tab-content resp-tab-content-active']//div[@class='attention closable'][normalize-space()='Pick a date by clicking on the text box.']")
frameLo=browser.find_element(By.XPATH,value="//div[@class='single_tab_div resp-tab-content resp-tab-content-active']//iframe[@class='demo-frame lazyloaded']")
browser.switch_to.frame(frameLo)
time.sleep(5)
browser.find_element(By.CSS_SELECTOR,value="#datepicker").click()
current_date=datetime.now()
# gave me the current date 
next_date=current_date+timedelta(days=1)
# current date+1
formatted_date=next_date.strftime("%m/%d/%y")
browser.find_element(By.CSS_SELECTOR,value="#datepicker").send_keys(formatted_date + Keys.TAB)
time.sleep(5)
browser.quit()