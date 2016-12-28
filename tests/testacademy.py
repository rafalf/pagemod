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
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from utils import reader
from utils import browser
from pages.home import Home
from pages.login import Login


class TestAcademy(unittest.TestCase):

    def setUp(self):

        self.conf = reader.get_conf()
        self.browser = self.conf.get('browser', 'Safari')
        self.locators = reader.get_locators()

        self.driver = browser.get_driver()

        self.driver.get(self.conf.get('site_url'))
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_01_register_validation(self):

        home = Home(self.driver, self.conf, self.locators)

        home.wait_page_loaded()

        home.select_get_involved()

    def test_02_login_validation(self):

        login = Login(self.driver, self.conf, self.locators)

        login.open_url(login.get_current_url() + '/login')

        login.wait_page_loaded()

        login.select_login()

        el = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'field-validation-error')))
        self.assertEqual(el.text, 'Please enter login name.')

        login.enter_user_name('user')

        login.select_login()

        el = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'field-validation-error')))
        self.assertEqual(el.text, 'Please enter a password.')

if __name__ == "__main__":

    suite = unittest.TestSuite()
    suite.addTest(TestAcademy("test_01_register_validation"))
    suite.addTest(TestAcademy("test_02_login_validation"))
    runner = unittest.TextTestRunner()
    runner.run(suite)