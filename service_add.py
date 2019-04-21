import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class testServices_add(unittest.TestCase):
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

        #Adding the service

        driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/div[2]/div/div/div/div/div[2]/div/div/p[2]/a').click()

        driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/div[3]/div/a/span').click()
        elem = driver.find_element_by_id('id_cust_name')
        elem.send_keys("Karnitha")
        elem = driver.find_element_by_id('id_service_category')
        elem.send_keys("Food/Catering")
        elem = driver.find_element_by_id('id_description')
        elem.send_keys("Lunch for MS graduates.Served at 12 PM, 04/29/2019")
        elem = driver.find_element_by_id('id_location')
        elem.send_keys("Scot cafe")
        elem = driver.find_element_by_id('id_service_charge')
        elem.send_keys(1800)
        driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/form/button').click()
        time.sleep(2)

        driver.get("https://anitha-mfscrm.herokuapp.com/home")
        assert "Logged In"

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()