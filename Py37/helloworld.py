from selenium import webdriver

driver = webdriver.Chrome()

driver.get("192.168.18.145")

print(driver.title)


