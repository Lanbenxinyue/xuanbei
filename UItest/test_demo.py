from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

# driver = webdriver.Chrome()
# driver.get("http://www.taobao.com")
import pytest

class TestClass:
        def test_one(self):
            x = "this"
            assert 'h' in x

        def test_two(self):
            x = 1
            assert x == 1

        def test_three(self):
            a = "hello"
            b = "hello world"
            assert a in b

if __name__ == "__main__":
    pytest.main(['-q','test_demo.py'])