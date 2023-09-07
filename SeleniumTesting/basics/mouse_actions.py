from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=opts)
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://testautomationpractice.blogspot.com/")

my_action=ActionChains(driver)
copy_text_button=driver.find_element(By.CSS_SELECTOR, '#HTML10 > div.widget-content > button')
my_action.double_click(copy_text_button).perform()

source=driver.find_element(By.ID, "draggable")
target=driver.find_element(By.ID, "droppable")
my_action.drag_and_drop(source, target).perform()

