from behave import given, when, then
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

my_assert=unittest.TestCase()
    
@given(u'User launches chrome browser')
def step_launch_browser(context):
    opts=webdriver.ChromeOptions()
    opts.add_experimental_option("detach", True)
    context.driver=webdriver.Chrome(options=opts)
    context.driver.maximize_window()
    context.driver.implicitly_wait(5)

@when(u'User navigates to OrangeHRM Site')
def step_navigate_to_orangehrm(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

@then(u'Validate whether user landed in OrangeHRM Site')
def step_validate_navigation(context):
    page_title=context.driver.title
    my_assert.assertEqual(page_title, "OrangeHRM", "Page title doesn't match")

@when(u'User logs in to OrangeHRM Site')    
def step_login_to_orangehrm(context):
    username_txtbx=context.driver.find_element(By.NAME,'username')
    username_txtbx.send_keys('Admin')
    password_txtbx=context.driver.find_element(By.NAME,'password')
    password_txtbx.send_keys('admin123')
    login_btn=context.driver.find_element(By.TAG_NAME, 'button')
    login_btn.click()
    
@then(u'User should be on Dashboard page')
def step_impl(context):
    pass
