import logging
from behave import given, when, then, step
from selenium import webdriver
from pages.loggedinPage import loggedinPage
from pages.abstract import *


@given(u'I launch "{browser_name}" browser')
def launch(context,browser_name):
    options = webdriver.ChromeOptions();
    exec_path_chrome = "Drivers/windows/chromedriver.exe"
    # exec_path_chrome = "Drivers/unix/chromedriver"
    options.add_experimental_option("detach", True)
    context.driver = webdriver.Chrome(options=options,executable_path=exec_path_chrome)
    context.driver.implicitly_wait(5)


@when(u'I goto "{url}" url')
def open_url(context,url):
    print("######################## Opening the URL .. ########################")
    context.driver.get(url)
    context.driver.maximize_window()


@when(u'I select "{dropDownValue}" from SortData dropdown')
def selectDropDownValue(context,dropDownValue):
    print("Selecing {} from SortData dropdown".format(dropDownValue))
    context.login_obj = loggedinPage(context.driver)
    context.login_obj.selectFromDropDown(dropDownValue)


@then(u'I close the browser')
def step_closeBrowser(context):
    print("Closing the Browser ..")
    context.driver.close()


@when(u'I store the original values for comparison')
def storeValues(context):
    context.login_obj = loggedinPage(context.driver)
    context.original_values = context.login_obj.fetchAndStoreValues()


@then(u'I verify that records are sorted by "{sortedbyValue}"')
def step_verifySorting(context,sortedbyValue):
    # print("context original valaues ---------------------",context.original_values,"\n\n\n")
    print("Verifying that records are sorted by: {}".format(sortedbyValue))
    context.login_obj = loggedinPage(context.driver)
    context.login_obj.verifySortAfterEnteringFilterValue(sortedbyValue);

@when(u'I enter "{filterInput}" into Filter Data')
def enterValue(context,filterInput):
    print("I am entering: {} into Filter Data".format(filterInput))
    context.login_obj = loggedinPage(context.driver)
    context.login_obj.enterIntoFilterData(filterInput)

@when(u'I verify that all records related to "{filterInput}" are returned')
def verifyRecordsReturned(context,filterInput):
    print("Verifying that all records related to {} are returned correctly".format(filterInput))
    context.login_obj = loggedinPage(context.driver)
    context.login_obj.verifyRecords(filterInput)


