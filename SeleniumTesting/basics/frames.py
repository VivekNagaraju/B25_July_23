from selenium import webdriver
from selenium.webdriver.common.by import By

opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=opts)
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://testautomationpractice.blogspot.com/")

driver.switch_to.frame("frame-one796456169")

txt_box_name=driver.find_element(By.ID, "RESULT_TextField-0")
txt_box_name.send_keys("Vivek")

frame_date_box= driver.find_element(By.ID, "RESULT_TextField-2")
frame_date_box.send_keys("09/06/2023")

driver.switch_to.parent_frame()

date_box= driver.find_element(By.ID, "datepicker")
date_box.send_keys("09/06/2023")
