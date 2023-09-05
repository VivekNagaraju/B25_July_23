from selenium import webdriver
from selenium.webdriver.common.by import By

opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=opts)
driver.maximize_window()
driver.get("https://www.google.com/")
sign_in=driver.find_element(By.CSS_SELECTOR, "#gb > div > div.gb_Md > a")
sign_in.click()
page_title=driver.title
print(page_title)
if page_title == "Sign in - Google Accounts":
    print("Sign in page Test passed")
    
else:
    print("Sign in page Test failed")
    
email=driver.find_element(By.ID, "identifierId")
email.send_keys("ahgf@gmail.com")


