from wjwliot.basic_action import initDriver
from wjwliot.basic_action import basicAction
from selenium import webdriver


basicAction.BaseAction.login(url="http://192.168.66.233:8080")

class page_department:
    def __init__(self, driver):
        self.driver = driver


    def add_department(self):
        # 进入单位模块
        self.driver.find_element_by_id("appendDivId").click()



pd = page_department
pd.add_department()