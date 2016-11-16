#!/usr/bin/env python

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import unittest
import getopt
import sys
import time
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

from utils import reader
from pages.home import Home


CHROME_DRIVER_PATH = 'C:\\Private Projects\\drivers\\chromedriver.exe'
IE_DRIVER_PATH = 'C:\\Private Projects\\drivers\\IEDriverServer.exe'
FIREFOX_BINARY = 'C:\\Program Files\\Mozilla Firefox\\firefox.exe'


class TestAcademy(unittest.TestCase):

    def __init__(self, test, browser):

        self.conf = reader.get_conf()
        self.locators = reader.get_locators()
        self.browser = browser
        super(TestAcademy, self).__init__(test)
    
    def setUp(self):

        if self.browser == 'Firefox':
            capabilities = webdriver.DesiredCapabilities().FIREFOX
            capabilities['acceptSslCerts'] = True
            binary = FirefoxBinary(FIREFOX_BINARY)
            self.driver = webdriver.Firefox(firefox_binary=binary, capabilities=capabilities)
        elif self.browser == 'Chrome':
            self.driver = webdriver.Chrome(CHROME_DRIVER_PATH)
        elif self.browser == 'Ie':
            capabilities = webdriver.DesiredCapabilities().INTERNETEXPLORER
            capabilities['acceptSslCerts'] = True
            self.driver = webdriver.Ie(executable_path=IE_DRIVER_PATH, capabilities=capabilities)
        elif self.browser == 'Safari':
            self.driver = webdriver.Safari()

        self.driver.get(self.conf.get('site_url'))
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def testRegister(self):

        home = Home(self.driver, self.conf, self.locators)

        home.wait_test_page_loaded()

        home.select_get_involved()


if __name__ == "__main__":

    # default browser
    browser = 'Safari'

    # parse args
    opts, args = getopt.getopt(sys.argv[1:], 'b:s', ['browser=', 'site='])
    for opt, arg in opts:
        if opt in ('-b', '--browser'):
            browser = arg
        elif opt in ('-s', '--site'):
            site = arg

    suite = unittest.TestSuite()
    suite.addTest(TestAcademy("testRegister", browser))
    runner = unittest.TextTestRunner()
    runner.run(suite)