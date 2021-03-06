import unittest
from testacademy import TestAPAValidation
import os
import HTMLTestRunner


def main():
    search_tests = unittest.TestLoader().loadTestsFromTestCase(TestAPAValidation)
    suite_tests = unittest.TestSuite([search_tests])

    with open(os.path.join(os.getcwd(), 'TestReport.html'), "w") as hlr:
        runner = HTMLTestRunner.HTMLTestRunner(stream=hlr, title='Test Report',description='Test Suite')
        runner.run(suite_tests)


if __name__ == "__main__":
    main()