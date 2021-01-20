import time

from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://192.168.66.233:8080")
driver.maximize_window()
# time.sleep(905)
# driver.get_screenshot_as_file('15分3秒截图.png')
# time.sleep(60)
# driver.get_screenshot_as_file('16分3秒截图.png')
# driver.quit()

def openWeb(url="http://192.168.66.233:8080"):
    driver = webdriver.Chrome()
    driver.get(url)
    driver.maximize_window()

def login(username="zongbu", password="1",url="http://192.168.66.233:8080"):
    openWeb(url)
    userna = driver.find_element_by_id('username')
    userna.send_keys(username)
    passwo = driver.find_element_by_id('password')
    passwo.send_keys(password)
    driver.find_element_by_id("btn_login").click()

