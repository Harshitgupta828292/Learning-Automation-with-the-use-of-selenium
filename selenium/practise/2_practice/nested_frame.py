


from selenium import webdriver
from selenium.webdriver.common.by import By
browser=webdriver.Firefox()
browser.maximize_window()
browser.get('https://the-internet.herokuapp.com/nested_frames')
#switching to to frames
browser.switch_to.frame("frame-top")
# switching to middle  frame
browser.switch_to.frame("frame-middle")
content=browser.find_element(By.ID,value="content").text
print("Content in middle frame",content)
# ?switch to default content
browser.switch_to.default_content()
# switch to bottom frame
browser.switch_to.frame("frame-bottom")
content_Bottom=browser.find_element(By.TAG_NAME,value="body").text
print("content in bottom frame",content_Bottom)


