from selenium import webdriver
import time
username="admin"
password="admin"
driver=webdriver.Firefox()
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
# https://username:password@domain/path
time.sleep(5)