import unittest
from selenium import webdriver
from PageObjects.login_page import LoginPage
from PageObjects.home_page import HomePage
from TestDatas import login_datas as ld
class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.get(ld.web_login_url)
        self.driver.maximize_window()
        self.lg=LoginPage(self.driver)

    def test_login(self):
        self.lg.login(ld.username,ld.password)
        self.assertTrue(HomePage(self.driver).isexist_logout_ele())

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)