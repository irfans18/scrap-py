# import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys

driver = Chrome()
driver.implicitly_wait(10)

url = 'https://twitter.com/'
driver.get(url)
# yield driver
# driver.quit()