import time


from wjwliot.basic_action.basicAction import BaseAction


class depPageAction(BaseAction):

    # def __init__(self,driver):
    #     self.driver = driver

    def get_into_dep(self):
        # 进入系统设置
        self.click_element(("xpath", "/html/body/aside[1]/div/dl[5]/dt/span"))
        time.sleep(2)
        # 进入单位信息管理
        self.click_element(("xpath", "//a[@data-title='单位信息管理']"))
        # self.driver.find_element_by_xpath("//a[@data-title='单位信息管理']").click()

    def add_dep(self):

        # 点击最高级别单位
        # self.click_element(("xpath", "//table[@id='treeTable1M']"))

        # 点击添加按钮
        self.click_element(("link_text", "添加下级"))
        # self.driver.find_element_by_link_text("添加下级").click()


