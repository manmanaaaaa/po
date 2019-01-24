# 快速复制  ctrl + d   删除 ctrl + y
from selenium.webdriver.common.by import By

#启动应用的包名和启动名
sms_app_package = "com.android.settings"
sms_app_activity = ".Settings"

#发送短信功能
sms_search = (By.ID,"com.android.settings:id/search")
sms_input_content = (By.ID,"android:id/search_src_text")
sms_btn_back = (By.CLASS_NAME,"android.widget.ImageButton")

#定位一组元素
# sms_send_lists = By.ID,"com.android.mms:id/text_view"

