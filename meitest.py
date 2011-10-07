import unittest
from test import test_meidocument
from test import test_meielement

def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(test_meidocument.suite())
    test_suite.addTest(test_meielement.suite())
    return test_suite
    
runner = unittest.TextTestRunner()
runner.run(suite())