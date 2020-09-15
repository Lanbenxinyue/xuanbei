from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Common.log_handler import logger


class HomePage:

    def __init__(self,driver):
        self.driver=driver
        #登录断言
    def isexist_logout_ele(self):
        #如果存在就返回Ture，如果不存在就返回False
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='currentChatLi']/i")))
            logger.info("断言成功，用例执行成功")
            return True
        except:
            logger.info("断言失败，用例执行失败")
            return False
        #新建工单断言
    def New_workorder(self):
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[5]/div/div")))
            logger.info("断言成功，用例执行成功")
            return True
        except:
            logger.info("断言失败，用例执行失败")
            return False
        #编辑工单状态和优先级断言
    def zt_workorder(self):
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='batchEditOrder']/button")))
            return True
        except:
            return False
        #批量派单断言
    def pd_workorder(self):
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='turnBtn']/div")))
            return True
        except:
            return False