from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=opts)
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://demo.automationtesting.in/Resizable.html")

my_action=ActionChains(driver)
home=driver.find_element(By.XPATH, "/html/body/header/nav/div/div[2]/ul/li[1]/a")
my_action.move_to_element(home).perform()