import unittest
import time
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
        driver.get("https://anitha-mfscrm.herokuapp.com/home/admin")
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id=\"content-main\"]/div[2]/table/tbody/tr[1]/td[1]/a').click()
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        time.sleep(1)

        time.sleep(2)
        with open('C:\Users\Anitha\Desktop\Spring 2019\MSD_ISQA8210\HW\Customercsv.csv') as csvDataFile:
            csvReader = csv.DictReader(csvDataFile)
            for row in csvReader:

                elem = driver.find_element_by_id('id_cust_name')
                elem.send_keys(row['name'])
                time.sleep(2)
                elem = driver.find_element_by_id('id_organization')
                elem.send_keys(row['organization'])
                elem = driver.find_element_by_id('id_role')
                elem.send_keys(row['role'])
                elem = driver.find_element_by_id('id_bldgroom')
                elem.send_keys(row['building'])
                elem = driver.find_element_by_id('id_account_number')
                elem.send_keys(row['acc_no'])
                elem = driver.find_element_by_id('id_address')
                elem.send_keys(row['address'])
                elem = driver.find_element_by_id('id_city')
                elem.send_keys(row['city'])
                elem = driver.find_element_by_id('id_state')
                elem.send_keys(row['state'])
                elem = driver.find_element_by_id('id_zipcode')
                elem.send_keys(row['zip'])
                elem = driver.find_element_by_id('id_email')
                elem.send_keys(row['email'])
                elem = driver.find_element_by_id('id_phone_number')
                elem.send_keys(row['phone'])
                driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/form/button').click()
                time.sleep(2)
        # deleting the created customers
        for i in range(3):
            driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/div[3]/table/tbody/tr[4]/td[13]/a').click()
            alert_obj = driver.switch_to.alert
            alert_obj.accept()
            time.sleep(2)

    def tearDown(self):
                self.driver.close()

if __name__ == "__main__":
                unittest.main()

