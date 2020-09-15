
"全局共享配置文件"
import pytest
from selenium import webdriver
from PageObjects.login_page import LoginPage
from TestDatas import Global_Datas as GD

@pytest.fixture()
def init_driver():# 访问网址全局配置
    driver = webdriver.Chrome()
    driver.get(GD.web_login_url)
    driver.maximize_window()

    yield driver

    driver.quit()

@pytest.fixture()
def init_login(init_driver):# 登录全局配置
    lg = LoginPage(init_driver)
    lg.login(GD.username, GD.password)

    yield init_driver

    init_driver.quit()