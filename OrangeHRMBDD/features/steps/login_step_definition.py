from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

@given(u'User launches chrome browser')
def step_launch_browser(context):
    opts=webdriver.ChromeOptions()
    opts.add_experimental_option("detach", True)
    context.driver=webdriver.Chrome(options=opts)
    context.driver.maximize_window()

@when(u'User navigates to OrangeHRM Site')
def step_navigate_to_orangehrm(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

@then(u'Validate whether user landed in OrangeHRM Site')
def step_validate_navigation(context):
    pass
