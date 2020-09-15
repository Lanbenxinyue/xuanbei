from PageLocators.login_page_locs import LoginPageLocs as Loc
from Common.basepage import BasePage
from PageLocators.order_page_locs import WorkorderLocator as WL

class OrderPage(BasePage):

    def order(self):


        self.click_element(WL.workorder, doc="工单中心_点击工单中心按钮")
        self.switch_iframe(WL.workorder_iframe,doc="工单中心_切换工单中心iframe")
