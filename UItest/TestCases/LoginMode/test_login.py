import allure
import pytest
from PageObjects.login_page import LoginPage
from PageObjects.home_page import HomePage
from TestDatas import Global_Datas as GD

@pytest.fixture
def init(init_driver):
    lg = LoginPage(init_driver)
    yield init_driver,lg  #init driver对象  lg页面对象

@allure.feature("登录模块")
@allure.story("测试用例小模块-登录案例")
@pytest.mark.usefixtures("init")
class TestLogin:

    @allure.title("测试用例名称：坐席登录工作台")
    def test_login(self,init):
        init[1].login(GD.username,GD.password)
        assert (HomePage(init[0]).isexist_logout_ele())


if __name__ == '__main__':
    pytest.mark(['-q','test_login.py'])