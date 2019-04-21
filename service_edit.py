import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class testServices_edit(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_blog(self):
        user = "instructor"
        pwd = "instructor1a"
        driver = self.driver
        driver.maximize_window()
        driver.get("https://anitha-mfscrm.herokuapp.com/home/")
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="myNavbar"]/ul[2]/li/a').click()
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        time.sleep(1)

        #Editing the service
        driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/div[2]/div/div/div/div/div[2]/div/div/p[2]/a').click()
        driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/div[3]/table/tbody/tr/td[8]/a').click()
        time.sleep(2)
        driver.find_element_by_id('id_service_charge').clear()
        time.sleep(2)
        elem = driver.find_element_by_id('id_service_charge')
        elem.send_keys("7000")
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/form/button').click()
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
        unittest.main()