'''import selenium
import pytest
from selenium import webdriver


driver = webdriver.Chrome(executable_path="/home/abdullah/PycharmProjects/pythonProject_2/Drivers/chromedriver_linux64 (1)/chromedriver")
driver.get("https://jobxprss.com/")
print("Title of the page is :" + driver.title)
driver.close()


if __name__ == "__main__":
    pytest.main()
'''

import selenium
import pytest
from selenium import webdriver
class Search_Engine:
    def Title_of_the_page(self):
        self.driver = webdriver.Chrome(executable_path="/home/abdullah/PycharmProjects/pythonProject_2/Drivers/chromedriver_linux64 (1)/chromedriver")
        self.driver.get("https://google.com")
        print("The page title of the google is " + self.driver.title)
        self.driver.close()

    def Title_of_the_linkedin(self):
        self.driver = webdriver.Chrome(executable_path="/home/abdullah/PycharmProjects/pythonProject_2/Drivers/chromedriver_linux64 (1)/chromedriver")
        self.driver.get("https://www.linkedin.com/")
        print("The page title of the google is " + self.driver.title)
        self.driver.close()
test_object = Search_Engine()
test_object.Title_of_the_page()
test_object.Title_of_the_linkedin()


