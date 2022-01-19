class ProxyMetaclass(type):
    def __new__(mcs, name, bases, attrs):
        count = 0
        attrs['__CrawlFunc__'] = []
        for k, v in attrs.items():
            if 'crawl_' in k:
                attrs['__CrawlFunc__'].append(k)
                count += 1
        attrs['__CrawlFuncCount__'] = count
        return type.__new__(mcs, name, bases, attrs)


class Crawler(object, metaclass=ProxyMetaclass):
    def get_proxies(self, callback):
        proxies = []
        for proxy in eval("self.{}()".format(callback)):  # 调用所有以crawl开头的方法
            print('成功获取代理', proxy)
            proxies.append(proxy)
        return proxies

    def crawl_daili66(self):
        for i in range(9):
            yield i

    def crawl_mmm(self):
        for i in ['afs', 'sdgf', 'sadgf']:
            yield i


class Getter:
    def __init__(self):
        self.crawler = Crawler()

    def run(self):
        print('获取器开始执行')
        for callback_label in range(self.crawler.__CrawlFuncCount__):
            callback = self.crawler.__CrawlFunc__[callback_label]
            proxies = self.crawler.get_proxies(callback)
            print(proxies)


if __name__ == '__main__':
    getter = Getter()
    getter.run()
