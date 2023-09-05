from selenium import webdriver
from selenium.webdriver.common.by import By

opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=opts)
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
alert_button=driver.find_element(By.CSS_SELECTOR, "#HTML9 > div.widget-content > button:nth-child(1)")
alert_button.click()
alert_text=driver.switch_to.alert.text
print(alert_text)
driver.switch_to.alert.accept()