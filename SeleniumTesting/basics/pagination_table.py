from selenium import webdriver
from selenium.webdriver.common.by import By

opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=opts)
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")

rows=driver.find_elements(By.XPATH, "//table[@id='productTable']/tbody/tr")
rows_count=len(rows)
for r in range(1, rows_count+1):
    product_cell=driver.find_element(By.XPATH, f"//table[@id='productTable']/tbody/tr[{r}]/td[2]")
    product_name=product_cell.text
    print(product_name)
    if product_name =="Product 4":
        check_box=driver.find_element(By.XPATH, f"//table[@id='productTable']/tbody/tr[{r}]/td[4]/input")
        check_box.click()
        break