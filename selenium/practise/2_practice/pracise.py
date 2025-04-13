from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
import time
driver=webdriver.Firefox()
driver.get("https://www.youtube.com/")
driver.maximize_window()

search_field=driver.find_element(By.NAME,value="search_query")
search_field.send_keys("apna collage java")
search_field.send_keys(Keys.RETURN)
time.sleep(2)
Click_field=driver.find_element(By.XPATH,value="//ytd-channel-name[@id='channel-title']//yt-formatted-string[@id='text']")
Click_field.click()

Video_Field=driver.find_element(By.role,value="button")
Video_Field.click()

time.sleep(5)
driver.quit()
