import datetime
import time


from Common import dir_config
from Common.log_handler import logger
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

#封装基本函数 - 执行日志 - 异常处理 - 失败截图
#所有页面公共的部分
class BasePage:

    def __init__(self,driver):
        self.driver=driver


    #等待元素可见
    def wait_eleVisible(self,locator,times=15,poll_frequency=0.5,doc=""):
        logger.info("{}:等待元素{}可见".format(doc,locator))
        try:
            start=datetime.datetime.now()
            WebDriverWait(self.driver, times,poll_frequency).until(EC.visibility_of_element_located(locator))
            end=datetime.datetime.now()
            wait_time=(end-start).seconds
            logger.info("{0} :元素{1}已可见 ，等待起始时间：{2}，等待结束时间：{3}， 等待时长为：{4}秒".format(doc,locator,start,end,wait_time))
        except:
            logger.exception("等待元素可见失败!!!")
            self.save_screenshot(doc)
            raise

    #等待元素存在
    def wait_elePresence(self,locator,times=15,poll_frequency=0.5,doc=""):
        logger.info("{0}:等待元素{1}存在".format(doc,locator))
        try:
            start = datetime.datetime.now()
            WebDriverWait(self.driver, times,poll_frequency).until(EC.presence_of_element_located(locator))
            end = datetime.datetime.now()
            wait_time = (end - start).seconds
            logger.info("等待结束，等待时长为：{}秒".format(wait_time))
        except:
            logger.exception("等待元素存在失败!!!")
            self.save_screenshot(doc)
            raise

    #查找元素
    def get_element(self,locator,doc=""):
        logger.info("{0}:查找元素:{1}".format(doc,locator))
        try:
            return  self.driver.find_element(*locator)
        except:
            logger.exception("查找元素失败!!!")
            self.save_screenshot(doc)
            raise

    #查找匹配元素
    def get_elements(self, locator, doc=""):
        logger.info("{0}:查找所有匹配的元素:{1}".format(doc, locator))
        try:
            return self.driver.find_elements(*locator)
        except:
            logger.exception("查找元素失败!!!")
            self.save_screenshot(doc)
            raise

    #点击操作
    def click_element(self,locator,times=15,poll_frequency=0.5,doc=""):
        self.wait_eleVisible(locator,times,poll_frequency,doc)
        ele = self.get_element(locator,doc)
        logger.info("{0}:点击元素:{1}".format(doc, locator))
        try:
            ele.click()
        except:
            logger.exception("元素点击操作失败!!!")
            self.save_screenshot(doc)
            raise

    #下拉框处理 index   通过索引位置
    def select_index(self,locator,num,times=15,poll_frequency=0.5,doc=""):
        self.wait_eleVisible(locator,times,poll_frequency,doc)
        ele = self.get_element(locator, doc)
        logger.info("{0}:下拉框索引选择元素:{1}".format(doc, locator))
        try:
            Select(ele).select_by_index(num)
        except:
            logger.exception("元素下拉框通过索引选择元素操作失败!!!")
            self.save_screenshot(doc)
            raise

    # 下拉框处理 text   通过下拉文本内容  "text"
    def select_text(self,locator,text,times=15,poll_frequency=0.5,doc=""):
        self.wait_eleVisible(locator,times,poll_frequency,doc)
        ele = self.get_element(locator, doc)
        logger.info("{0}:下拉框text选择元素:{1}".format(doc, locator))
        try:
            Select(ele).select_by_visible_text(text)
        except:
            logger.exception("元素下拉框通过text选择元素操作失败!!!")
            self.save_screenshot(doc)
            raise

    # 下拉框处理 value   通过option value   "value"
    def select_value(self,locator,value,times=15,poll_frequency=0.5,doc=""):
        self.wait_eleVisible(locator,times,poll_frequency,doc)
        ele = self.get_element(locator,doc)
        logger.info("{0}:下拉框value选择元素:{1}".format(doc,locator))
        try:
            Select(ele).select_by_value(value)
        except:
            logger.exception("元素下拉框通过value选择元素操作失败!!!")
            self.save_screenshot(doc)
            raise

    #输入操作
    def input_text(self,locator,text,times=15, poll_frequency=0.5, doc=""):
        self.wait_eleVisible(locator,times,poll_frequency,doc)
        ele = self.get_element(locator,doc)
        logger.info("{0}:输入操作:{1}".format(doc,locator))
        try:
            ele.send_keys(text)
        except:
            logger.exception("元素输入操作失败!!!")
            self.save_screenshot(doc)
            raise

    #获取元素的文本内容
    def get_text(self,locator,times=15, poll_frequency=0.5, doc=""):
        self.wait_eleVisible(locator, times, poll_frequency, doc)
        ele = self.get_element(locator, doc)
        logger.info("在{0}获取元素:{1}的文本内容".format(doc,locator))
        try:
            return ele.text
        except:
            logger.exception("获取元素文本内容失败!!!")
            self.save_screenshot(doc)
            raise
    #获取元素的属性
    def get_element_attribute(self):
        pass

    #alert处理
    def alert_action(self,doc=""):
        ele = self.driver.switch_to.alert
        try:
            ele.accept()
        except:
            logger.exception("弹窗关闭失败!!!")
            self.save_screenshot(doc)
            raise

    #iframe处理
    def switch_iframe(self,iframe_reference,times=15,poll_frequency=0.5,doc=""):
        logger.info("{0}:等待表单元素{1}存在，并进入该表单.".format(doc,iframe_reference))
        try:
            start=datetime.datetime.now()
            WebDriverWait(self.driver,times,poll_frequency).until(EC.frame_to_be_available_and_switch_to_it(iframe_reference))
            end=datetime.datetime.now()
            wait_time=(end-start).seconds
            logger.info("等待结束，等待时长为：{}秒".format(wait_time))
        except:
            logger.info("等待表单元素失败!!!")
            self.save_screenshot(doc)
            raise
    #退回上层表单
    def switch_parent_iframe(self,doc=""):
        logger.info("{}退回上层表单".format(doc))
        self.driver.switch_to.parent_frame()
    #上传操作
    def upload_file(self):
        pass

    #截图操作
    def save_screenshot(self,doc):
        #图片名称  页面名称  操作名称   时间  png
        filePath= dir_config.screenshot_dir + "/{0}_{1}.png".format(doc, time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()))
        try:
            self.driver.save_screenshot(filePath)
            logger.info("截屏成功，文件路径为:{}".format(filePath))
        except:
            logger.info("截图失败")
       # datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S")

if __name__ == '__main__':
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    driver = webdriver.Chrome()
    driver.get("www.baidu.com")
    test = BasePage(driver)
    #test.