# 文档地址https://www.python-httpx.org/
import httpx  # pip install httpx # pip install httpx[http2]
import asyncio
import time

# headers = {'user-agent': 'my-app/1.0.0'}
# params = {'key1': 'value1', 'key2': 'value2'}
# cookies = {'color': 'green'}
# url = 'https://httpbin.org/get'
# r = httpx.get(url, headers=headers, params=params, cookies=cookies, timeout=3)
# print(r)
# print(r.status_code)  # 状态码
# print(r.encoding)  # 文本编码
# print(r.headers)
# print(r.cookies)
# print(r.text)
# print(r.json())


"""
httpx提供了Client来解决以上问题，Client是基于HTTP连接池实现的，
这意味着当你对一个网站发送多次请求的时候，Client会保持原有的TCP连接，从而提升程序的执行效率。
"""
# with httpx.Client() as client:
#     headers = {'X-Custom': 'value'}
#     r = client.get('https://example.com', headers=headers)
#     print(r.text)

"""
我们可以将headers、cookies、params等参数放在http.Client()中，在Client下的请求共享这些配置参数
可以看出，r1的请求头包含{'x-auth': 'from-client'}, r2虽然配置了headers2，
但由于里面的headers1和headers2的参数不同，Client会合并这两个headers的参数作为一个新的headers
（如果参数相同，则headers2的参数会覆盖headers1的参数）。
"""
# headers1 = {'x-auth': 'from-client'}
# params1 = {'client_id': '1234'}
# url = 'https://example.com'
# with httpx.Client(headers=headers1, params=params1) as client:
#     headers2 = {'x-custom': 'from-request'}
#     params2 = {'request_id': '4321'}
#     r1 = client.get(url)
#     print(r1.request.headers)
#     r2 = client.get(url, headers=headers2, params=params2)
#     print(r2.request.headers)


"""
httpx可以通过设置proxies参数来使用http代理，我们也可以使用不同的代理来分别处理http和https协议的请求
httpx的代理参数proxies只能在httpx.Client()中添加，client.get()是没有这个参数的。
"""
# proxies = {
#     'http://': 'http://119.23.40.47:8080',  # 代理1
#     'https://': 'http://119.23.40.47:8080',  # 代理2
# }
# url = 'https://example.com'
# with httpx.Client(proxies=proxies) as client:
#     r1 = client.get(url)
#     print(r1)

"""
当请求https协议的链接时，发出的请求需要验证所请求主机的身份，因此需要SSL证书来取得服务器的信任后。
如果要使用自定义的CA证书，则可以使用verify参数
"""
# r = httpx.get("https://example.org", verify="path/to/client.pem")
# #  或者可以完全禁用SSL验证（不推荐）。
# r = httpx.get("https://example.org", verify=False)

"""
使用async/await语句来进行异步操作，创建一个httpx.AsyncClient()对象
"""
# async def main():
#     async with httpx.AsyncClient() as client:  # 创建一个异步client
#         r = await client.get('https://www.example.com/')
#         print(r)
#
# asyncio.run(main())

"""
检查 HTTP 版本
在客户端启用 HTTP/2 支持并不一定意味着您的请求和响应将通过 HTTP/2 传输，因为客户端 和服务器都需要支持 HTTP/2。
如果您连接到仅支持 HTTP/1.1 的服务器，则客户端将改为使用标准 HTTP/1.1 连接。
可以通过检查.http_version响应上的属性来确定使用了哪个版本的 HTTP 协议。
"""
# client = httpx.Client(http2=True)
# response = client.get("https://www.baidu.com/")
# print(response.http_version)  # "HTTP/1.0", "HTTP/1.1", or "HTTP/2".

"""
一个异步请求栗子
"""
async def req(client, i):
    res = await client.get('https://www.example.com')
    print(f'第{i + 1}次请求，status_code = {res.status_code}')
    return res


async def main():
    async with httpx.AsyncClient() as client:
        task_list = []  # 任务列表
        for i in range(300):
            res = req(client, i)
            task = asyncio.create_task(res)  # 创建任务
            task_list.append(task)
        await asyncio.gather(*task_list)  # 收集任务


if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(f'异步发送300次请求，耗时：{end - start}')
