from selenium.webdriver.common.by import By


class WorkorderLocator:
    #判断工单中心元素
    workorder=(By.XPATH,"//*[@id='orderManageLi']/a")

    #工单中心iframe
    workorder_iframe="orderManageWindow"

    #工单中心选项按钮
    workorder_button=(By.XPATH,"/html/body/div[1]/div[1]/div[1]/div[3]")

    #工单中心新建工单按钮
    workroder_new=(By.XPATH, "//*[@id='addOrder']")

    #新建工单iframe
    new_ifrname="layui-layer-iframe1"

    #提单人下拉框
    new_tdr=(By.XPATH,"//*[@id='crmFields']/div[1]/div/div[1]/div/div[2]/span/span[1]/span")

    #提单人下拉框选择
    new_tdr_1=(By.XPATH,"//*[@id='select2-customerJID-results']/li[1]")

    #工单主题输入框
    new_zhuti=(By.XPATH,"//*[@id='subject']")

    #工单内容iframe
    new_text_iframe="description_ifr"

    #工单内容输入框
    new_text_1=(By.XPATH,"//body[@id='tinymce']")

    #新建工单保存按钮
    new_button=(By.XPATH,"//*[@id='saveOrderBtn']")

    #导入工单按钮
    import_button=(By.XPATH,"//*[@id='importBtn']")

    #导入工单iframe
    import_iframe="//iframe[@src='/page/order/importOrder.html']"

    #文件上传选择框
    import_updata=(By.XPATH,"//*[@id='importFile']")

    #上传工单模板地址
    moban="JiaxinAutotest/TestDatas/工单导入模板20200506115702.xlsx"

    #所有工单按钮
    all_workorder=(By.XPATH,"//*[@id='A390D0C4AFDE70159536']")

    #所有工单iframe
    all_workorder_iframe="//*[@id='frame-con']/iframe[9]"

    #选中全部工单
    workorder_1=(By.XPATH,"//*[@id='checkAll']")

    #批量编辑状态按钮
    bianji_button=(By.XPATH,"//*[@id='batchEditOrder']/button")

    #优先级下拉框
    youxianji=(By.XPATH,"//*[@id='order_priority']")

    #工单状态下拉框
    workorderzt=(By.XPATH,"//*[@id='order_status']")

    #批量编辑确定按钮
    bianji_button_1=(By.XPATH,"//*[@id='saveOrderBtn']")

    #批量派单按钮
    paidan_button=(By.XPATH,"//*[@id='turnBtn']/div")

    #批量派单确定按钮
    paidan_button_1=(By.XPATH,"//*[@id='dispatchOrderBtn']")