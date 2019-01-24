from base.base_action import BaseAction
import page
class SearchPage(BaseAction):
    #初始化方法
    def __init__(self,driver):
        BaseAction.__init__(self,driver)
    #
    def click_search(self):
        self.click_element(page.sms_search)

    #2.向搜索输入框里面输入内容
    def input_content(self,content):
        self.input_edit_content(page.sms_input_content,content)

    #3.返回
    def send_click_btn_back(self):
        self.click_element(page.sms_btn_back)


