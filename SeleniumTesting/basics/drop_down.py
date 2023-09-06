from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=opts)
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://testautomationpractice.blogspot.com/")

country_drop_down=driver.find_element(By.ID, "country")


country_selector=Select(country_drop_down)
# country_selector.select_by_visible_text("Australia")
# country_selector.select_by_index(5)
country_selector.select_by_value("uk")
