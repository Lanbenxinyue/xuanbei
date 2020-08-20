from selenium.webdriver.common.by import By

class LoginPageLocs:
    #账号输入框
    name_text=(By.XPATH,"//*[@id='username']")

    #密码输入框
    pwd_text=(By.XPATH,"//*[@id='password']")

    #登录按钮
    login_button=(By.XPATH,"//*[@id='submit']")

    #判断技能组元素
    jinengzu=(By.XPATH,"//*[@id='layui-layer-iframe4']")

    #技能组表单
    jnzbiaodan="layui-layer-iframe4"

    #选择技能组
    jnz_1=(By.XPATH,"//*[@id='test779']")

    #确定技能组按钮
    jnz_button=(By.XPATH,"/html/body/div[2]/button")
