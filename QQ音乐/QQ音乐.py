import requests
import execjs
import time

url = 'https://u.y.qq.com/cgi-bin/musics.fcg'
with open('QQ音乐.js', 'r', encoding='utf-8') as f:
    js = f.read()
# for i in range(0, 10):
data = '{"comm":{"cv":4747474,"ct":24,"format":"json","inCharset":"utf-8","outCharset":"utf-8","notice":0,"platform":"yqq.json","needNewCode":1,"uin":0,"g_tk_new_20200303":5381,"g_tk":5381},"req_1":{"module":"music.musichallSinger.SingerList","method":"GetSingerListIndex","param":{"area":-100,"sex":-100,"genre":-100,"index":1,"sin":0,"cur_page":1}}}:'
sign = execjs.compile(js).call('new_sign', data)
print(sign)
headers = {
    'cookie': 'RK=D8I8TxTyFF; ptcz=64d430dbdec10a22fa8d0ac78d3ad7c4bc845e162635f761b5f3a36d04a33fd1; LW_uid=E1n6f0h5p0O8n3z331Q551N1W8; eas_sid=11k6f0Y5g0C86373o125y1U4o1; pgv_pvi=4749412352; pgv_pvid=4136563820; tvfe_boss_uuid=f5207ef4e7c0a172; Qs_lvt_323937=1611586279%2C1613353135; Qs_pv_323937=3395662713140043300%2C1135970460013982200%2C3951656303194131500; LW_sid=y1G66183Q3W5y3i2Z6j8z3L4E3; pac_uid=0_da19931c92a92; ts_uid=8704797443; fqm_pvqid=0f43b591-1bb8-46d3-8d6b-e6e86104a6cf; fqm_sessionid=313796c8-0dac-4496-bbd9-aa29d6a8aecd; pgv_info=ssid=s5703926680; ts_last=y.qq.com/n/ryqq/singer_list; ts_refer=i.y.qq.com/',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
    'sec-ch-ua-mobile': '?0',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
}
params = {
    '_': str(time.time() * 1000),
    'sign': 'zzad80ncjf8jtfsod0292e31337866814fcbca32d9fd237d'
}
content = requests.get(url, params=params, headers=headers, data=data).json()
print(content)