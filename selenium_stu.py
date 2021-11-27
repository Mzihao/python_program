# -*- coding:UTF-8 -*-
from selenium import webdriver
from selenium.webdriver import ActionChains
import time
browser = webdriver.Chrome()
browser.maximize_window()
'''
browser.get('https://www.taobao.com')
input = browser.find_element_by_id('q')
input.send_keys('iphone')
import time
time.sleep(3)
input.clear()
input.send_keys('airpods')
time.sleep(5)
button = browser.find_element_by_class_name('btn-search')
button.click()
# browser.close()
'''


#模拟鼠标拖拽
browser.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
browser.switch_to_frame('iframeResult')
source = browser.find_element_by_css_selector('#draggable')
target = browser.find_element_by_css_selector('#droppable')
actions = ActionChains(browser)
actions.drag_and_drop(source, target)
actions.perform() # 执行鼠标操作

'''
#拖动到底部
browser.get('https://www.zhihu.com/')
time.sleep(2)
#browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
browser.execute_script('window.scrollTo(document.body.scrollWidth,document.body.scrollHeight)')
# browser.execute_script('alert("TO Bottom")')
'''

'''
browser.get('https://www.zhihu.com/')
time.sleep(2)
input = browser.find_element_by_class_name('SignFlow-submitButton')
print(input.get_attribute('class')) #获取属性
print(input.text) #获取文本
'''

#前进和后退
# browser.get('https://www.taobao.com')
# browser.get('https://www.baidu.com')
# browser.get('https://www.jd.com')
# browser.back()
# time.sleep(2)
# browser.forward()
# browser.close()