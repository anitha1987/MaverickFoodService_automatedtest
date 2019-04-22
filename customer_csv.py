import unittest
import time
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class testCustomer_csv(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_Edit(self):
        user = "instructor"
        pwd = "instructor1a"
        driver = self.driver
        driver.maximize_window()
        driver.get("https://anitha-mfscrm.herokuapp.com/admin")
        time.sleep(5)
        # driver.find_element_by_xpath('//*[@id=\"content-main\"]/div[2]/table/tbody/tr[1]/td[1]/a').click()
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id=\"content-main\"]/div[2]/table/tbody/tr[1]/td[1]/a').click()
        time.sleep(2)
        with open('C:\\Users\\Anitha\\Desktop\\MaverickFoodService\\Test Suite\\customer_details.csv') as csvDataFile:
            csvReader = csv.DictReader(csvDataFile)
            for row in csvReader:

                elem = driver.find_element_by_id('id_cust_name')
                elem.send_keys(row['Cust_name'])
                time.sleep(2)
                elem = driver.find_element_by_id('id_organization')
                elem.send_keys(row['Organization'])
                elem = driver.find_element_by_id('id_role')
                elem.send_keys(row['Role'])
                elem = driver.find_element_by_id('id_email')
                elem.send_keys(row['Email'])
                elem = driver.find_element_by_id('id_bldgroom')
                elem.send_keys(row['BldgRoom'])
                elem = driver.find_element_by_id('id_address')
                elem.send_keys(row['Address'])
                elem = driver.find_element_by_id('id_account_number')
                elem.send_keys(row['Account_No'])
                elem = driver.find_element_by_id('id_city')
                elem.send_keys(row['City'])
                elem = driver.find_element_by_id('id_state')
                elem.send_keys(row['State'])
                elem = driver.find_element_by_id('id_zipcode')
                elem.send_keys(row['Zipcode'])
                elem = driver.find_element_by_id('id_phone_number')
                elem.send_keys(row['Phone Number'])
                driver.find_element_by_xpath('//*[@id="customer_form"]/div/div/input[1]').click()
                driver.find_element_by_xpath('//*[@id="content-main"]/ul/li/a').click()
                time.sleep(2)


    def tearDown(self):
                self.driver.close()

if __name__ == "__main__":
                unittest.main()

