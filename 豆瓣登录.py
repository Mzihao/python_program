from selenium import webdriver
import time

driver = webdriver.Chrome()

# 登录豆瓣网
driver.get("https://www.douban.com/")
time.sleep(1)
# 切换到登录框架中来
iframe = driver.find_element_by_tag_name("iframe")
driver.switch_to.frame(iframe)
time.sleep(1)
# 输入"账号密码"
driver.find_element_by_class_name("account-tab-account").click()
driver.find_element_by_id("username").send_keys("18475030859")
driver.find_element_by_id("password").send_keys("mmm123456")
# 点击登录按钮
driver.find_element_by_class_name("account-form-field-submit").click()
# 退出
#time.sleep(10)
#driver.close()