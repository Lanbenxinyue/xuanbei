import allure
import pytest
from PageObjects.order_page import OrderPage
from PageObjects.home_page import HomePage
from TestDatas import Global_Datas as GD

@pytest.fixture
def init(init_login):
    order = OrderPage(init_login)
    yield init_login,order  #init driver对象  lg页面对象

@allure.feature("工单中心模块")
@allure.story("测试用例小模块-工单案例")
@pytest.mark.usefixtures("init")
class Testorder:

    @allure.title("测试用例名称：坐席新建工单")
    def test_order(self,init):
        init[1].order()
        assert (HomePage(init[0]).New_workorder())


if __name__ == '__main__':
    pytest.mark(['-q','test_login.py'])