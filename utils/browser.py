from . import reader
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


def get_driver():

    browser = reader.get_conf().get('browser', 'Chrome')

    if browser == 'Firefox':
        binary = FirefoxBinary(reader.get_conf().get('ff_driver'))
        driver = webdriver.Firefox(firefox_binary=binary)
    elif browser == 'Chrome':
        driver = webdriver.Chrome(reader.get_conf().get('chrome_driver'))
    elif browser == 'Ie':
        driver = webdriver.Ie(executable_path=reader.get_conf().get('ie_driver'))
    elif browser == 'Safari':
        driver = webdriver.Safari()
    return driver