import unittest

from unittestpackage.test_case_demo import TestCaseDemo
from unittestpackage.test_case_demo2 import TestCaseDemo2

# get all tests from Test case  demo and Test case demo2

tc1 = unittest.TestLoader().loadTestsFromTestCase(TestCaseDemo)
tc2 = unittest.TestLoader().loadTestsFromTestCase(TestCaseDemo2)

# create a test suite combining Test Case Demo and Test Case demo 2

smoke_test = unittest.TestSuite([tc1, tc2])

# trigger the run

unittest.TextTestRunner(verbosity=2).run(smoke_test)

