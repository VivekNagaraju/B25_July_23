'''
https://www.google.com/
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=opts)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.google.com/")

text_area=driver.find_element(By.ID, "APjFqb")
text_area.send_keys("amazon")

amazon=driver.find_element(By.ID, "jZ2SBf")
amazon.click()