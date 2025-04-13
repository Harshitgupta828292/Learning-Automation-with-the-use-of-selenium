from selenium import webdriver
from selenium.webdriver.common.by import By
browser=webdriver.Firefox()
browser.maximize_window()
browser.get('https://www.selenium.dev/')
browser.switch_to.new_window()
browser.get('https://playwright.dev/')
number_of_tabs=len(browser.window_handles)
print(number_of_tabs)
tabs_value=browser.window_handles
print(tabs_value)
Current_tab=browser.current_window_handle
print(Current_tab)
browser.find_element(By.CSS_SELECTOR,value=".getStarted_Sjon").click()
FirstTab=browser.window_handles[0]
if Current_tab !=FirstTab:
    browser.switch_to.window(FirstTab)
browser.find_element(By.XPATH,value="//span[normalize-space()='Downloads']").click()