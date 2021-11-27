import requests, execjs

url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'

headers = {
    'Cookie': 'BIDUPSID=AC2B25A8B486C63D84BFB30EE05B7E7D; PSTM=1600848360; BAIDUID=D299D5728A2CF5E6F8344E716DC7FEB1:FG=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; __yjs_duid=1_d4f38ffef0db537fa940e7f06c28cf661619589350550; H_WISE_SIDS=107319_110085_127969_128698_131423_154214_165136_166148_170142_170817_170936_171234_171509_171573_172472_172644_172867_173016_173633_174036_174324_174436_174449_174549_174638_174662_174665_174694_174856_174909_175030_175045_175213_175275_175284_175365_175555_175730_175749_175819_175859_175899_175974; BDUSS=R6ekFKWnJoZ2JwS0VvQkgyMmhOVWtGZk04cWx-QjFTU0xsQU85ZHJOVn5iOGhnRVFBQUFBJCQAAAAAAAAAAAEAAAAVxpHLbXpowvMxMgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAH~ioGB~4qBgNW; BDUSS_BFESS=R6ekFKWnJoZ2JwS0VvQkgyMmhOVWtGZk04cWx-QjFTU0xsQU85ZHJOVn5iOGhnRVFBQUFBJCQAAAAAAAAAAAEAAAAVxpHLbXpowvMxMgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAH~ioGB~4qBgNW; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BAIDUID_BFESS=D299D5728A2CF5E6F8344E716DC7FEB1:FG=1; H_PS_PSSID=34099_31254_34004_33607; delPer=0; PSINO=7; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; BCLID=11212164697627500158; BDSFRCVID=Z8kOJexroG38EYQek3MVboKjOLweG7bTDYLEOwXPsp3LGJLVJeC6EG0Pts1-dEu-EHtdogKK3gOTH4PF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tRk8oI0aJDvVeJ5mMtTJqR08hxb-2J0XKKOLVMoStp7ketn4hUt5e--QjUoQtjOzKDOiBJo7an5zMnr2QhrdQjDwjGJNLUnL2gor-J3C2bjpsIJM5-nHQP00BgcyhTv4aKviaKOjBMb1MMJDBT5h2M4qMxtOLR3pWDTm_q5TtUJMeCnTDMFhe6oM-l-X5to05TIX3b7EfMFWjp7_bJ7KhUbye-okQ4QWt2jp3J7c2q7dfn5jjP5xQhFTQtnfXpOe-n7rKhc1QqcqEIQHQT3m5bJLqfO4-Cr4WTnbWb3cWKOJ8UbSjh3PBTD02-nBat-OQ6npaJ5nJq5nhMJmb67JDMr0exbH55uttbIqoU5; BCLID_BFESS=11212164697627500158; BDSFRCVID_BFESS=Z8kOJexroG38EYQek3MVboKjOLweG7bTDYLEOwXPsp3LGJLVJeC6EG0Pts1-dEu-EHtdogKK3gOTH4PF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF_BFESS=tRk8oI0aJDvVeJ5mMtTJqR08hxb-2J0XKKOLVMoStp7ketn4hUt5e--QjUoQtjOzKDOiBJo7an5zMnr2QhrdQjDwjGJNLUnL2gor-J3C2bjpsIJM5-nHQP00BgcyhTv4aKviaKOjBMb1MMJDBT5h2M4qMxtOLR3pWDTm_q5TtUJMeCnTDMFhe6oM-l-X5to05TIX3b7EfMFWjp7_bJ7KhUbye-okQ4QWt2jp3J7c2q7dfn5jjP5xQhFTQtnfXpOe-n7rKhc1QqcqEIQHQT3m5bJLqfO4-Cr4WTnbWb3cWKOJ8UbSjh3PBTD02-nBat-OQ6npaJ5nJq5nhMJmb67JDMr0exbH55uttbIqoU5; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1623235227; BA_HECTOR=2g0gagal2g2kag211o1gc17gg0r; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1623236590; __yjs_st=2_YTQwYzVmZTg0MTNmNGE0MzI1ODA5NDcwZmJkM2U5ZDNkMTQ1ZTUxNTFlOWRkNWU3OTI2OTVjZTVlZGUwY2FiMWJhNzllYWI3YzNjOWVkYmMyYzcwMjdmN2M4MGVhNTA1ZjIyNjc4OTllNTllMmM0MGE2ODBjYTkyNmU4NmE3MGY3NWY2YWViNTFjYmZlMjdkY2VjMGRmZjUzODBkZjg5OWZmY2JkMjFkMGMxYWExMjE5NDZhZWU1NzNjYmQzYzU1ZDE1MjA2ODI3OWY0MTFlNGEyZGUyNWRlMmRmMjdjODM3OTk5NWFmNGJmNzllNzEyNjk1NWZlYjkyYmM1NWZiZl83XzI5ZmJlMjVj; ab_sr=1.0.1_YTkwYjllZjQ5ODliYzNmNTM0OTU4OGNhYzEyYzE1OTQ5MmE2MjdlMGU3YmY0Y2M0YzE5N2M0MjhjZmY2YjlmNGMzNTY0ZGViMzgwY2JhYmVjNzRiOWNmZjk0ZDAzNjdiZGNmMTM1MjBhNmQ1ODEwMzQwMzJiZjUxMmJjMmEyNmVmNjEzOTU4OTZiZTE5ZTBiN2QyMjI0ZDE5MGRjOGJlN2FlZmYxZjRjNjAwNjU3Y2VhZTAxZDUxNzBlNzliYjQ5',
    'Host': 'fanyi.baidu.com',
    'Origin': 'https://fanyi.baidu.com',
    'Referer': 'https://fanyi.baidu.com/?aldtype=16047',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
    'sec-ch-ua-mobile': '?0',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}

def get_sign(kw):
    with open('sign.js', 'r', encoding='utf-8') as f:
        js = f.read()
    sign = execjs.compile(js).call('e', kw)
    return sign

def translate(kw, sign):
    data = {
        'from': 'en',
        'to': 'zh',
        'query': kw,
        'transtype': 'realtime',
        'simple_means_flag': '3',
        'sign': sign,
        'token': '2c9fe1a0b20c7f3047e8aeb995d484f1',
        'domain': 'common',
    }
    res = requests.post(url,headers=headers, data=data).json()
    result = res['trans_result']['data'][0]['dst']
    print(result)

if __name__ == '__main__':
    while 1:
        kw = input("请输入你要翻译的英文：")
        # kw = "yellow"
        sign = get_sign(kw)
        translate(kw, sign)
