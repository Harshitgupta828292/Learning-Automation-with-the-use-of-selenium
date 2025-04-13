import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 

browser=webdriver.Firefox()
browser.get('https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407')
browser.maximize_window()
time.sleep(5)
browser.execute_script("window.scrollTo(0,document.body.scrollHeight);")
# browser.find_element(By.XPATH,value="//label[normalize-space()='Sunday']")

# browser.find_element(By.XPATH,value="//label[normalize-space()='Sunday']").click()
checkboxes=browser.find_elements(By.XPATH,"//input[@type='checkbox']")
# time.sleep(5)
for checkbox in checkboxes:
    
    checkbox.send_keys(Keys.SPACE)
checked_count=0
for checkbox in checkboxes:
    if checkbox.is_selected():
        checked_count +=1
expected_checked_count= 7
if checked_count ==expected_checked_count:
    print('Checkedbox count verified')
else:
    print('checkboxes count mismise')
time.sleep(5)
browser.close()
                     