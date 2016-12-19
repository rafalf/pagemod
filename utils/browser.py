from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


def get_driver(conf):

    if conf.get('browser') == 'Firefox':
        binary = FirefoxBinary(conf.get('firefox_binary'))
        driver = webdriver.Firefox(firefox_binary=binary)
    elif conf.get('browser') == 'Chrome':
        driver = webdriver.Chrome(conf.get('chrome_driver'))
    elif conf.get('browser') == 'Chrome-OSX':
        driver = webdriver.Chrome()
    elif conf.get('browser') == 'Ie':
        driver = webdriver.Ie(executable_path=conf.get('ie_driver'))
    elif conf.get('browser') == 'Safari':
        driver = webdriver.Safari()
    return driver