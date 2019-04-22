import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class testCustomer_add(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_blog(self):

       user = "instructor"
       pwd = "instructor1a"
       name = "Anitha"
       organization = "UNO"
       role = "Student"
       email = "test123@test.com"
       bldgroom = "ABC"
       address = "3rd street"
       accountnumber = "00000"
       city = "omaha"
       state = "NE"
       zipcode = "00000"
       phone = "1234"



       #Opening browser & maximizing window
       driver = self.driver
       driver.fullscreen_window()


       #logging in to the admin page
       driver.get("https://anitha-mfscrm.herokuapp.com/admin/")
       time.sleep(2)
       elem = driver.find_element_by_id("id_username")
       elem.send_keys(user)
       time.sleep(2)
       elem = driver.find_element_by_id("id_password")
       elem.send_keys(pwd)
       time.sleep(2)
       elem.send_keys(Keys.RETURN)
       time.sleep(2)
       assert "Logged In"


       #Adding a new Customer
       elem = driver.find_element_by_xpath("//*[@id=\"content-main\"]/div[2]/table/tbody/tr[1]/td[1]/a")
       elem.click()
       elem = driver.find_element_by_id("id_cust_name")
       elem.send_keys(name)
       elem = driver.find_element_by_id("id_organization")
       elem.send_keys(organization)
       elem = driver.find_element_by_id("id_role")
       elem.send_keys(role)
       elem = driver.find_element_by_id("id_email")
       elem.send_keys(email)
       elem = driver.find_element_by_id("id_bldgroom")
       elem.send_keys(bldgroom)
       elem = driver.find_element_by_id("id_address")
       elem.send_keys(address)
       elem = driver.find_element_by_id("id_account_number")
       elem.send_keys(accountnumber)
       elem = driver.find_element_by_id("id_city")
       elem.send_keys(city)
       elem = driver.find_element_by_id("id_state")
       elem.send_keys(state)
       elem = driver.find_element_by_id("id_zipcode")
       elem.send_keys(zipcode)
       elem = driver.find_element_by_id("id_phone_number")
       elem.send_keys(phone)
       elem = driver.find_element_by_xpath("//*[@id=\"customer_form\"]/div/div/input[1]")
       elem.click()
       time.sleep(2)
       driver.get("https://anitha-mfscrm.herokuapp.com/customer_list")
       time.sleep(2)
       assert "Posted New Test Customer"




   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
   unittest.main()
