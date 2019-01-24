
import time
class BaseAction:
    def __init__(self,driver):
        self.driver = driver


    def find_element(self, loc):
        time.sleep(1)
        return self.driver.find_element(loc[0], loc[1])


    def find_elements(self,loc):
        time.sleep(1)
        return self.driver.find_elements(loc[0],loc[1])

    #点击元素的方法
    def click_element(self,loc):
        self.find_element(loc).click()

    #向输入框里面输入内容
    def input_edit_content(self,loc,content):
        input_element = self.find_element(loc)
        input_element.clear()
        input_element.send_keys(content)



