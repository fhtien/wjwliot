import os, sys
sys.path.append(os.getcwd())
import time
from wjwliot.basic_action.initDriver import init_driver
from wjwliot.modules.page_depInfo import depPageAction



class TestDep:
    def setup(self):
        self.driver = init_driver()
        self.driver.get("localhost:8080")
        # self.driver.get("http://192.168.18.95:8080/system/DepartmentList1")
        self.dep = depPageAction(self.driver)
        self.dep.click_element(("id", "username"))
        self.dep.send_keys(("id", "username"), 'zongbu')
        self.dep.click_element(("id", "password"))
        self.dep.send_keys(("id", "password"), '1')
        self.dep.click_element(("id", "btn_login"))
        self.driver.maximize_window()
        # self.driver.implicitly_wait(7)
        time.sleep(5)

        print('setup结束')

    def test_add_dep(self):
        self.dep.get_into_dep()

        self.dep.change_frame(("xpath", "//iframe[@src='/system/DepartmentList1']"))

        self.dep.add_dep()



    def teardown(self):
        time.sleep(3)
        self.driver.quit()


if __name__ =="__main__":
    obj = TestDep()
    obj.setup()
    obj.test_add_dep()
    obj.teardown()
