import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

LOGIN = ''
PASSWORD = ''

options = webdriver.ChromeOptions()
binary_yandex_driver_file = 'C:/Users/User/AppData/Local/Yandex/YandexBrowser/Application/browser.exe'

class TestAuthYA(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('C:/Users/User/AppData/Local/Yandex/YandexBrowser/Application/browser.exe', options=options)

    def test_login_success(self):
        self.driver.get('https://passport.yandex.ru/auth/')
        self.assertIn('Авторизация', self.driver.title)
        elem = self.driver.find_element('login')
        elem.send_keys(LOGIN)
        elem.send_keys(Keys.RETURN)
        self.driver.implicitly_wait(10)
        elem = self.driver.find_element("input#passp-field-passwd")
        elem.send_keys(PASSWORD)
        elem.send_keys(Keys.RETURN)
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()