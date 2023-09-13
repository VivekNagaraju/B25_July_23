import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestOrangeHRM(unittest.TestCase):


    def test_navigation(self):
        opts=webdriver.ChromeOptions()
        opts.add_experimental_option("detach", True)
        driver=webdriver.Chrome(options=opts)
        driver.maximize_window()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        page_title=driver.title
        self.assertEqual(page_title, "OrangeHRM123", "Page title doesn't match")
        
        
        
    def test_login(self):
        opts=webdriver.ChromeOptions()
        opts.add_experimental_option("detach", True)
        driver=webdriver.Chrome(options=opts)
        driver.maximize_window()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()