from selenium import webdriver
from selenium.webdriver.common.by import By

opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=opts)
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")

print("Book Name", "Price")
for a in range(2, 8):
    book=driver.find_element(By.CSS_SELECTOR, f"#HTML1 > div.widget-content > table > tbody > tr:nth-child({a}) > td:nth-child(1)")
    book_name=book.text
    print(book_name, end=" ")
    # if book_name=="Master In Selenium":
    price=driver.find_element(By.CSS_SELECTOR, f"#HTML1 > div.widget-content > table > tbody > tr:nth-child({a}) > td:nth-child(4)")
    print(price.text)