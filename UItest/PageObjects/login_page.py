from PageLocators.login_page_locs import LoginPageLocs as Loc
from Common.basepage import BasePage

class LoginPage(BasePage):

    def login(self,username,password):

        self.input_text(Loc.name_text,username,doc="登录页面_输入用户名")
        self.input_text(Loc.pwd_text,password,doc="登录页面_输入密码")
        self.click_element(Loc.login_button,doc="登录页面_点击登录")
        # self.switch_iframe(Loc.jnzbiaodan,doc="客服工作台_切换技能组表单")
        # self.click_element(Loc.jnz_1,doc="客服工作台_选择技能组")
        # self.click_element(Loc.jnz_button,doc="客服工作台_确定技能组")

