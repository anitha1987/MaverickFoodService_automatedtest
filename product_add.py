import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class testProduct_add(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_blog(self):
        user = "instructor"
        pwd = "instructor1a"
        driver = self.driver
        driver.maximize_window()
        driver.get("https://anitha-mfscrm.herokuapp.com/home/")
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="myNavbar"]/ul[2]/li/a').click()
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        time.sleep(1)

        #Adding the product

        driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/div[2]/div/div/div/div/div[3]/div/div/p[2]/a').click()

        driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/div[3]/div/a/span').click()
        elem = driver.find_element_by_id('id_cust_name')
        elem.send_keys("James")
        elem = driver.find_element_by_id('id_product')
        elem.send_keys("05467")
        elem = driver.find_element_by_id('id_p_description')
        elem.send_keys("Ice cream has been added")
        elem = driver.find_element_by_id('id_quantity')
        elem.send_keys("3")
        elem = driver.find_element_by_id('id_charge')
        elem.send_keys("1000")
        driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/form/button').click()
        time.sleep(2)

        driver.get("https://anitha-mfscrm.herokuapp.com/home")
        assert "Logged In"

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()