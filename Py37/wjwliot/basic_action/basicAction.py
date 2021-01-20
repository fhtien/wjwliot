import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


class BaseAction:
    def login(self, url="http://192.168.66.233:8080", username='zongbu', password="1"):

        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        usn = self.driver.find_element_by_id("username")
        usn.send_keys(username)
        psw = self.driver.find_element_by_id('password')
        psw.send_keys(password)

        self.driver.find_element_by_id("btn_login").click()

    def __init__(self, driver):
        self.driver = driver

    def click_element(self,feature):
        self.find_element(*feature).click()

    def find_element(self, *feature):

        try:
            # 确保元素是可见的。
            # 注意：以下入参为元组的元素，需要加*。Python存在这种特性，就是将入参放在元组里。
            #      WebDriverWait(self.driver,10).until(lambda driver: driver.find_element(*loc).is_displayed())
            # 注意：以下入参本身是元组，不需要加*
            WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(feature))
            return self.driver.find_element(*feature)
        except:
            print(u"%s 页面中未能找到 %s 元素" % (self, feature))


    def send_keys(self, feature, value):
        self.find_element(*feature).send_keys(value)

    def change_frame(self, index):
        self.driver.switch_to.frame(index)

    def gen_images(self):
        try:
            pass
        except:
            pass
