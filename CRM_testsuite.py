from unittest import TestLoader, TestSuite, TextTestRunner


from customer_add import testCustomer_add
from customer_edit import testCustomer_edit
from customer_delete import testCustomer_delete
from service_add import testServices_add
from service_edit import testServices_edit
from service_delete import testServices_delete
from product_add import testProduct_add
from product_edit import testProduct_edit
from product_delete import testProduct_delete



if __name__ == "__main__":
    loader = TestLoader()
    suite = TestSuite((
        loader.loadTestsFromTestCase(testCustomer_add),
        loader.loadTestsFromTestCase(testCustomer_edit),
        loader.loadTestsFromTestCase(testCustomer_delete),
        loader.loadTestsFromTestCase(testServices_add),
        loader.loadTestsFromTestCase(testServices_edit),
        loader.loadTestsFromTestCase(testServices_delete),
        loader.loadTestsFromTestCase(testProduct_add),
        loader.loadTestsFromTestCase(testProduct_edit),
        loader.loadTestsFromTestCase(testProduct_delete),


    ))

    runner = TextTestRunner(verbosity=2)
    runner.run(suite)