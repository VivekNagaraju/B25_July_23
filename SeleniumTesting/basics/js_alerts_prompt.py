from selenium import webdriver
from selenium.webdriver.common.by import By

opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=opts)
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
prompt_box=driver.find_element(By.CSS_SELECTOR, "#HTML9 > div.widget-content > button:nth-child(3)")
prompt_box.click()

driver.switch_to.alert.send_keys("Vivek")
driver.switch_to.alert.accept()