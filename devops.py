from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
import time
options = Options()
driver = webdriver.Edge(options=options)
driver.get("https://www.google.com")
time.sleep(50)
search_box = driver.find_element(By.NAME, "q")
print("Tag Name:", search_box.tag_name)
print("Element Text:", search_box.text)
print("Displayed:", search_box.is_displayed())
print("Enabled:", search_box.is_enabled())
print("Outer HTML:", search_box.get_attribute("outerHTML"))
time.sleep(5)
driver.quit()