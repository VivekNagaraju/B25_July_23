from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin

opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=opts)
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")

resizable=driver.find_element(By.ID, "resizable")
my_action=ActionChains(driver)
my_action.scroll_to_element(resizable).perform()
my_action.scroll_by_amount(0, 150).perform()
# my_action.scroll_from_origin(ScrollOrigin(resizable), 0, 150).perform()