# 导入selenium工具
from selenium import webdriver
# 导入解析xml的库
from lxml import etree

class Huya(object):
    # 初始化
    def __init__(self):
        option = webdriver.ChromeOptions() # 给Chrom的运行添加参数
        option.add_argument('headless') # 使用headless(无界面)打开
        self.driver = webdriver.Chrome(chrome_options=option) # 将参数对象传入Chrome，则启动了无界面的Chrome

        #初始化要统计的数据
        self.roomcount = 0 #直播间数量
        self.roomhot = 0 #直播间人气热度总量

    # 开始爬虫
    def run(self):
        # 打开网页
        self.driver.get('https://www.huya.com/l')
        page = 0
        while True:
            # 延迟一下
            import time
            time.sleep(1)
            page += 1
            # 爬取相关的内容
            content = etree.HTML(self.driver.page_source) #获取并解析网页源码 <Element html at 0x20f06d98e00>
            #爬取房间的信息 先找到父节点
            rooms = content.xpath('//li[@class="game-live-item"]')
            # print(len(rooms))
            for room in rooms:
                # 爬取房间名称
                tmp = room.xpath('./a[@class="title"]/@title') # 返回列表
                if len(tmp) > 0:
                    roomname = tmp[0]

                # 爬取房间人气
                tmp = room.xpath('./span[@class="txt"]/span[@class="num"]/i[@class="js-num"]/text()')
                if len(tmp) > 0:
                    hot = tmp[0]

                print('房间人气:%s,房间名称:%s' % (hot,roomname))
                # 增加房间数量
                self.roomcount += 1
                # 增加人气数
                if hot[-1] == '万':
                    if len(hot) == 7:
                        hot = (10000+hot[2:-1])*10000
                    else:
                        hot = hot[:-1]
                        hot = int(float(hot) * 10000)
                    self.roomhot += hot
                else:
                    self.roomhot += int(hot)

            ret = self.driver.page_source.find('laypage_next') #查看有无下一页按钮
            if ret > 0:
                print('第%d页' % page)
            else:
                print('最后一页')
                break
            # 点击下一页按钮
            self.driver.find_element_by_class_name('laypage_next').click()


        #输出结果
        print('当前直播间房间数量:%d' % self.roomcount)
        print('当前直播间人气热度总数:%d' % self.roomhot)

    # 测试代码
    def test(self):
        # 打开网页
        self.driver.get('https://www.huya.com/l')
        page = 0
        while True:
            # 延迟一下
            import time
            time.sleep(2)

            page += 1
            ret = self.driver.page_source.find('laypage_next')
            if ret > 0:
                print('第%d页' % page)
            else:
                print('最后一页')
                break
            # 点击下一页按钮
            self.driver.find_element_by_class_name('laypage_next').click()

if __name__ == '__main__':
    huya = Huya()
    huya.run()
    #huya.test()