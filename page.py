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
import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os


class Page(unittest.TestCase):

    def __init__(self, driver, conf, locators):
        self.driver = driver
        self.conf = conf
        self.locators = locators

    def _wait_page_loaded(self, selector_css):
        try:
            WebDriverWait(self.driver, int(self.conf.get('page_timeout'))).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, selector_css)), 'element timed out: %s' % selector_css)
        except TimeoutException as e:
            self.fail(e)

    def take_screenshot(self, file_name):
        self.driver.save_screenshot(os.path.join(self.conf.get('temp_path'), file_name))

    def open_url(self, url):
        self.driver.get(url)

    def get_current_url(self):
        return self.driver.current_url

    def get_validation_error(self):

        try:
            selector = 'field-validation-error'
            return WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, selector)), 'element timed out: %s' % selector)
        except TimeoutException as e:
            self.fail(e)

    def get_element_by_css(self, selector_css):

        try:
            return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((
                By.CSS_SELECTOR, selector_css)), 'element timed out: %s' % selector_css)
        except TimeoutException as e:
            self.fail(e)

    def wait_for_element_by_css(self, selector_css):

        try:
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((
                By.CSS_SELECTOR, selector_css)), 'element timed out: %s' % selector_css)
        except TimeoutException as e:
            self.fail(e)

    def switch_to_registration_frame(self):

        try:
            selector_css = '#registerFrame'
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((
                By.CSS_SELECTOR, selector_css)), 'element timed out: %s' % selector_css)

            self.driver.switch_to_frame('registerFrame')
        except TimeoutException as e:
            self.fail(e)