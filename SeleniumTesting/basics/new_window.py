from selenium import webdriver
from selenium.webdriver.common.by import By
import time

"""1. Launchung chrome browser"""
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=opts)
driver.maximize_window()
driver.implicitly_wait(10)

"""2. Navigate to Practice Site"""
driver.get("https://testautomationpractice.blogspot.com/")
print(driver.current_window_handle)

"""3. Type "Selenium" in wikipedia searxh box and click on "Selenium in Biology" """
wiki_search_box=driver.find_element(By.ID, "Wikipedia1_wikipedia-search-input")
wiki_search_box.send_keys("Selenium")
wiki_search_icon=driver.find_element(By.CLASS_NAME,"wikipedia-search-button")
wiki_search_icon.click()
# time.sleep(5)
search_result=driver.find_element(By.LINK_TEXT, "Selenium in biology")
search_result.click()

"""4. Switch to new window"""
windows=driver.window_handles
print(windows)
driver.switch_to.window(windows[1])
print(driver.current_window_handle)
# indicator_plants=driver.find_element(By.CSS_SELECTOR,"#toc-Indicator_plants > a")
# indicator_plants.click()

