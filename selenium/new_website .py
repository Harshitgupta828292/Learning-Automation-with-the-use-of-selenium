from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


driver.get("https://trytestingthis.netlify.app/index.html")
driver.find_element(By.ID, "fname").send_keys("harshit")
driver.find_element(By.ID, "lname").send_keys("gupta")
time.sleep(5)
driver.find_element(By.XPATH, "//button[@class=class='btn btn-success']").click()
time.sleep(5)
