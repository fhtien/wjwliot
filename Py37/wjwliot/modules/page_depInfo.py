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

    def add_dep(self):

        # 点击最高级别单位
        self.click_element(("xpath", "//table[@id='treeTable1M']"))

        # 点击添加按钮
        self.click_element(("xpath", "/html/body/div[1]/div[2]/span[1]/a"))

        # 切换到添加窗口
        self.change_frame(("xpath", '//*[@src="/system/DepartmentEdit?supdeptid=A26F7C8B-0BA1-446A-BD50-3C77BDA67B29&sszq=&deptCode=59XX"]'))

        # 填写单位名称
        self.send_keys(("xpath", '//*[@id="deptName"]'), "蓝翔支队")  # 批量数据

        # 选择单位类别
        self.click_element(("xpath", '//*[@id="departmentForm"]/div[4]/div[1]/span/span/span/a'))
        self.click_element(("id", "_easyui_tree_538"))  # 批量数据

        # 跳出iframe才能点确定
        self.driver.switch_to.parent_frame()

        # 点击确定
        self.click_element(("xpath", '//*[@class="layui-layer layui-layer-iframe"]/div[3]/a[1]'))

