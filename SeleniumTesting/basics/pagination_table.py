from selenium import webdriver
from selenium.webdriver.common.by import By

opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=opts)
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")

rows=driver.find_elements(By.XPATH, "//table[@id='productTable']/tbody/tr")
rows_count=len(rows)

'''
# Pagination using nested For-Loop
pages=driver.find_elements(By.CSS_SELECTOR, "#pagination > li")
page_count=len(pages)

for a in range(1, page_count+1):
    next_page= driver.find_element(By.CSS_SELECTOR, f"#pagination > li:nth-child({a}) > a")
    next_page.click()
    clicked=False
    for r in range(1, rows_count+1):
        product_cell=driver.find_element(By.XPATH, f"//table[@id='productTable']/tbody/tr[{r}]/td[2]")
        product_name=product_cell.text
        print(product_name)
        if product_name =="Product 12":
            check_box=driver.find_element(By.XPATH, f"//table[@id='productTable']/tbody/tr[{r}]/td[4]/input")
            check_box.click()
            clicked=True
            break
    if clicked == True:
        break
'''  

# Pagination using nested While-Loop 
while True:
    clicked=False
    for r in range(1, rows_count+1):
        product_cell=driver.find_element(By.XPATH, f"//table[@id='productTable']/tbody/tr[{r}]/td[2]")
        product_name=product_cell.text
        print(product_name)
        if product_name =="Product 12":
            check_box=driver.find_element(By.XPATH, f"//table[@id='productTable']/tbody/tr[{r}]/td[4]/input")
            check_box.click()
            clicked=True
            break
        
    if clicked == True:
        break
    next_page= driver.find_element(By.XPATH, "//a[@class='active']//parent::li//following-sibling::li[1]/a")
    next_page.click()







