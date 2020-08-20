from PageLocators.login_page_locs import LoginPageLocs as Loc
from Common.basepage import BasePage

class LoginPage(BasePage):

    def login(self,username,password):
        doc="登录页面_登录功能"
        self.wait_eleVisible(Loc.name_text,doc=doc)
        self.input_text(Loc.name_text,username,doc=doc)
        self.input_text(Loc.pwd_text,password,doc=doc)
        self.click_element(Loc.login_button,doc=doc)
        self.wait_eleVisible(Loc.jinengzu,doc=doc)
        self.switch_iframe(Loc.jnzbiaodan,doc=doc)
        self.wait_eleVisible(Loc.jnz_1,doc=doc)
        self.click_element(Loc.jnz_1,doc=doc)
        self.click_element(Loc.jnz_button,doc=doc)

