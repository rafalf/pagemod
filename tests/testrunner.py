import unittest
from testacademy import TestAcademy
import os
import HTMLTestRunner


def main():
    search_tests = unittest.TestLoader().loadTestsFromTestCase(TestAcademy)
    suite_tests = unittest.TestSuite([search_tests])

    dir = os.getcwd()
    with open(os.path.join(os.getcwd(), 'TestReport.html'), "w") as hndlr:
        runner = HTMLTestRunner.HTMLTestRunner(stream = hndlr,title = 'Test Report',description = 'Test Suite')
        runner.run(suite_tests)


if __name__ == "__main__":
    main()