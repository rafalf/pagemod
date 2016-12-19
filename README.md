## Links and configuration:

__Chrome driver:__
* https://sites.google.com/a/chromium.org/chromedriver/downloads

__Chrome driver - OS X:__
* https://sites.google.com/a/chromium.org/chromedriver/downloads
* cp chromedriver /usr/local/bin

__To test:__  
```python```
```from selenium import webdriver```
```driver = webdriver.Chrome()```

__Firefox:__
* https://github.com/mozilla/geckodriver/releases/
* https://developer.mozilla.org/en-US/docs/Mozilla/QA/Marionette/WebDriver

__Ie:__
* Set the correct zoom: http://stackoverflow.com/questions/12034969/internetexplorerdriver-zoom-level-error
* http://stackoverflow.com/questions/31134408/unable-to-find-element-on-closed-window-on-ie-11-working-with-selenium  - uncheck on all zones
* https://github.com/SeleniumHQ/selenium/wiki/InternetExplorerDriver - win32 ( 62 bit is slow )

__Safari:__
* https://webkit.org/blog/6900/webdriver-support-in-safari-10/

## Main concepts:
* actions (click, send_keys and so on): on the class page level
* verifications (asserts): on the test level

## Run test suite and generate HTML report:
* testrunner.py

