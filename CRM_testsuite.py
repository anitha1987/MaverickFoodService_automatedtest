from unittest import TestLoader, TestSuite, TextTestRunner
from customer_add import testCustomer_add
from WebAutomation.Test.Scripts.Edit_Customer import Edit_Customer
from WebAutomation.Test.Scripts.Delete_Customer import Delete_Customer
from WebAutomation.Test.Scripts.Customer_Summary import Customer_Summary
from WebAutomation.Test.Scripts.services_add import services_add
from WebAutomation.Test.Scripts.services_edit import services_edit
from WebAutomation.Test.Scripts.services_delete import services_delete
from WebAutomation.Test.Scripts.Add_Product import Add_Product
from WebAutomation.Test.Scripts.Edit_Product import Edit_Product
from WebAutomation.Test.Scripts.Delete_Product import Delete_Product
from WebAutomation.Test.Scripts.Add_Customer_Admin import Add_Customer_Admin
from WebAutomation.Test.Scripts.Add_Service_Admin import Add_Service_Admin
from WebAutomation.Test.Scripts.customers_add_csv import customer_add

if __name__ == "__main__":
    loader = TestLoader()
    suite = TestSuite((
        loader.loadTestsFromTestCase(testCustomer_delete),
        loader.loadTestsFromTestCase(Edit_Customer),
        loader.loadTestsFromTestCase(Delete_Customer),
        loader.loadTestsFromTestCase(Customer_Summary),
        loader.loadTestsFromTestCase(services_add),
        loader.loadTestsFromTestCase(services_edit),
        loader.loadTestsFromTestCase(services_delete),
        loader.loadTestsFromTestCase(Add_Product),
        loader.loadTestsFromTestCase(Edit_Product),
        loader.loadTestsFromTestCase(Delete_Product),
        loader.loadTestsFromTestCase(Add_Customer_Admin),
        loader.loadTestsFromTestCase(Add_Service_Admin),
        loader.loadTestsFromTestCase(customer_add),
    ))

    runner = TextTestRunner(verbosity=2)
    runner.run(suite)