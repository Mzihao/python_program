from selenium import webdriver
import time

driver = webdriver.Chrome()

# 登录淘宝网
driver.get("https://login.taobao.com/")

# 输入"账号密码"
driver.find_element_by_id("fm-login-id").send_keys("麦mzh")
driver.find_element_by_id("fm-login-password").send_keys("mzh19980112")

# 点击登录按钮
driver.find_element_by_class_name('fm-button').click()