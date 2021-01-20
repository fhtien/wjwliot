import time

from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://192.168.18.145:8080")
driver.maximize_window()
username = driver.find_element_by_id('username')
username.send_keys('zongbu')
password = driver.find_element_by_id('password')
password.send_keys('1')

driver.find_element_by_id("btn_login").click()

time.sleep(15)

# 进入库室维护模块
driver.find_element_by_xpath('/html/body/aside[1]/div/dl[4]/dt').click()
time.sleep(2)
driver.find_element_by_xpath('//a[@data-href="/system/SysDepotInfo"]').click()
time.sleep(2)

# driver.find_element_by_xpath('//*[@id="treeRightDiv"]/div/div[2]/span[1]/a[1]/a[@class="btn btn-primary radius " and @avalon-events="click:eclick_0_roomAdd4039503944392815521152242112346039443947system47SysDepotInfoEdit3944393944393941"]').click()
# driver.find_element_by_xpath('//*[@id="treeRightDiv"]/div/div[2]/span[1]/a[1]/text()').click()

js = 'document.getElementById("rootDeptID").nextElementSibling.click();'
driver.execute(js).click()

time.sleep(3)
driver.quit()