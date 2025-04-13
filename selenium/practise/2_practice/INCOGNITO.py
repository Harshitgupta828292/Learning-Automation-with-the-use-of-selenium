from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
Firefox_options=Options()
Firefox_options.add_argument("--private")
driver=webdriver.Firefox(options=Firefox_options)
driver.maximize_window()
time.sleep(15)
driver.get("https://www.google.com/")
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# import time
# chrome_options=Options()
# chrome_options.add_argument("--incognito")
# driver=webdriver.Chrome(options=chrome_options)
# driver.maximize_window()
# time.sleep(5)
# driver.get("https://www.google.com/")