from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# 2. Screen full
driver.maximize_window()

driver.get("https://demo.opencart.com/index.php?route=account/login")

# Invalid Test
driver.find_element(By.ID, 'input-email').clear()
driver.find_element(By.ID, 'input-email').send_keys("invalidemail@test.com")
driver.find_element(By.ID, 'input-password').clear()
driver.find_element(By.ID, 'input-password').send_keys("saas23142134")
driver.find_element(By.XPATH, '//*[@id="content"]/div/div[2]/div/form/input').click()

# Valid Test
driver.find_element(By.ID, 'input-email').clear()
driver.find_element(By.ID, 'input-email').send_keys("user6@bd.com")
driver.find_element(By.ID, 'input-password').clear()
driver.find_element(By.ID, 'input-password').send_keys("123456")
driver.find_element(By.XPATH, '//*[@id="content"]/div/div[2]/div/form/input').click()


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)