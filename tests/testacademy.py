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

from utils import reader
from utils import browser

from pages.home import Home
from pages.login import Login
from pages.register import Register


class TestAPAValidation(unittest.TestCase):

    def setUp(self):

        self.conf = reader.get_conf()
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

        register = Register(self.driver, self.conf, self.locators)

        register.select_register()

        register.switch_to_registration_frame()

        register.enter_email('bademail@')

        register.select_next()

        el = register.get_validation_error()

        self.assertEqual(el.text, 'Please enter a valid email address.')

    def test_02_login_validation(self):

        login = Login(self.driver, self.conf, self.locators)

        login.open_url(login.get_current_url() + 'login')

        login.wait_page_loaded()

        login.select_login()

        el = login.get_validation_error()

        self.assertEqual(el.text, 'Please enter login name.')

        login.enter_user_name('user')

        login.select_login()

        el = login.get_validation_error()

        self.assertEqual(el.text, 'Please enter a password.')

if __name__ == "__main__":

    suite = unittest.TestSuite()
    suite.addTest(TestAPAValidation("test_01_register_validation"))
    suite.addTest(TestAPAValidation("test_02_login_validation"))
    runner = unittest.TextTestRunner()
    runner.run(suite)