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
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from page import Page


class Home(Page, unittest.TestCase):

    def __init__(self, driver, conf, locators):
        self.driver = driver
        self.conf = conf
        self.locators = locators

    def wait_page_loaded(self):
        try:
            selector_css = self.locators.get('register')
            WebDriverWait(self.driver, int(self.conf.get('page_timeout'))).until(EC.presence_of_element_located((By.CSS_SELECTOR, selector_css)),
                                                    message='element timed out: %s' % selector_css)
        except TimeoutException as e:
            self.fail(e)

    def select_get_involved(self):
        selector_css = self.locators.get('register')
        self.get_element_by_css(selector_css).click()

