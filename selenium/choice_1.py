from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time 
driver=webdriver.Firefox()
driver.maximize_window()
login_url="https://the-internet.herokuapp.com/dropdown"
driver.get(login_url)

dropdown_element=driver.find_element(By.ID,value="dropdown")
# select=Select(dropdown_element)
# option_count=len(select.options)
# #select the value of visible set
# # select the value by index
# # se;ect thevalue by using the value 
# # select.select_by_index("2")
# # select.select_by_visible_text("Option 2")
# expected_count=3
# if option_count==expected_count:
#     print("test case ")
# else:
#     print("test case fail")
target_value="Option 2"
select=Select(dropdown_element)
for option in select.options:
    if option.text ==target_value:
        option.click()
        print(f"Selected Option is {target_value}")
        break
    else:
        print(f"option'{target_value}'not found")
    # how  to select select class
    # how to interact with breakdown 
    # select by visible text