import selenium
import pytest
from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="/home/abdullah/PycharmProjects/pythonProject_2/Drivers/chromedriver_linux64 (1)/chromedriver")
driver.maximize_window()

driver.get("https://demo.opencart.com/")

My_Account = driver.find_element_by_class_name("dropdown")
My_Account.click()
driver.find_element_by_css_selector("#top-links > ul > li.dropdown.open > ul > li:nth-child(1) > a").click()
driver.find_element_by_id("input-firstname").send_keys("Md. Abdullah")
driver.find_element_by_id("input-lastname").send_keys("Al Baky")
driver.find_element_by_id("input-email").send_keys("mrk3218@gmail.com")
driver.find_element_by_id("input-telephone").send_keys("01689062047")
driver.find_element_by_id("input-password").send_keys("abcd1055")
driver.find_element_by_id("input-confirm").send_keys("abcd1055")
driver.find_element_by_name("agree").click()
driver.find_element_by_class_name("btn.btn-primary").click()

#driver.close()