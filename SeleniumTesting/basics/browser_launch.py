from selenium import webdriver
from selenium.webdriver.common.by import By

opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=opts)
driver.maximize_window()
driver.get("https://www.google.com/")
sign_in=driver.find_element(By.CSS_SELECTOR, "#gb > div > div.gb_Md > a > span")
sign_in.click()