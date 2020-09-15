import pytest


pytest.main(["-s","-v","--html=Outputs/reports/test_report.html","--alluredir=./Outputs/allure_reports"])

#allure serve Outputs/allure_reports   #allure 服务端口执行

#"--reruns" ,"2"  设置失败用例重跑 "--reruns-delay","5" 重跑用例间隔时间

