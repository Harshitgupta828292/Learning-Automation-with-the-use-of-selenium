# # from selenium import webdriver


# # driver=webdriver.Chrome()
# # driver.get("https://www.youtube.com/")


# # # location element from html



# # from selenium import webdriver
# # from selenium.webdriver.common.keys import Keys
# # from selenium .webdriver.common.by import By
# # import time
# # driver=webdriver.Chrome()

# # driver.get("https://www.python.org/")
# # assert "python" in driver.title
# # elem=driver.find_element(By.NAME,"q")
# # elem.clear()
# # elem.send_keys("hjddhjdfjklsdf")
# # elem.send_keys(Keys.RETURN)
# # assert "no result found" not in driver.page_source
# # time .sleep(10)
# # driver.close()
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://google.com")
time.sleep(5)
driver.close()
driver.quit()
print("done")
