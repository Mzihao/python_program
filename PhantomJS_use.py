# 导入selenium工具
from selenium import webdriver
# 通过浏览器加载网页
# driver = webdriver.PhantomJS()
# driver = webdriver.Chrome() # 使用普通浏览器打开
option = webdriver.ChromeOptions()
option.add_argument('headless')
driver = webdriver.Chrome(chrome_options=option)  #使用headless打开
# 打开网页
driver.get('https://www.baidu.com/')
# 截图
driver.save_screenshot('C:/Users/admin/Desktop/爬的东西/phantomjs/baidu1.png')

# 找到要搜索的输入框控件
driver.find_element_by_id('kw').send_keys('张家辉')
# 截图
driver.save_screenshot('C:/Users/admin/Desktop/爬的东西/phantomjs/baidu2.png')
# 找到要点击的控钮控件
driver.find_element_by_id('su').click()
# 延迟1秒
import time
time.sleep(1)
# 截图
driver.save_screenshot('C:/Users/admin/Desktop/爬的东西/phantomjs/baidu3.png')