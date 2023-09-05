from selenium import webdriver
from selenium.webdriver.common.by import By

opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=opts)
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
confirm_box=driver.find_element(By.CSS_SELECTOR, "#HTML9 > div.widget-content > button:nth-child(2)")
confirm_box.click()
driver.switch_to.alert.dismiss()

confirm_message=driver.find_element(By.ID, "demo").text
print(confirm_message)

if confirm_message == "You pressed OK!":
    print("Test case Passed!")
    
else:
    print("Test case Failed!")