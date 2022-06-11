from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# 2. Screen full
driver.maximize_window()

driver.get("https://www.w3schools.com/python/")
driver.find_element_by_link_text("Python.HOME").click()