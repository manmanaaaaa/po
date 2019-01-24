import os,sys

from virtualenv import read_data

sys.path.append(os.getcwd())
import pytest

from page.search_page import SearchPage
from base.init_driver import get_driver
from base.read_yaml import read_yaml_data
import page

def read_yaml_file():
    return read_yaml_data("sms_send.yaml").get("send_data")

class TestSearch:

    def setup_class(self):
        #1.初始化driver
        self.driver = get_driver(page.sms_app_package,page.sms_app_activity)
        #2.初始化smspage类
        self.page = SearchPage(self.driver)

    def test_send(self):
        self.page.click_search()

    #测试短信业务方法
    @pytest.mark.parametrize("content", read_yaml_file())
    def test_send_sms(self,content):
        self.page.input_content(content)

    def test_sms(self):
        self.page.send_click_btn_back()

    def teardown_class(self):
        self.driver.quit()

