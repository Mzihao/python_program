import requests
import re
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def get_hash_album():
    url = 'https://www.kugou.com/yy/rank/home/1-8888.html?from=rank'
    html = session.get(url, headers=headers, verify=False).text
    pat = '{"Hash":"(.*?)",'
    pat2 = '"album_id":(.*?),"'
    hash_list = re.compile(pat).findall(html)
    album_list = re.compile(pat2).findall(html)
    # print(hash_list)
    # print(album_list)
    return hash_list, album_list

def get_json(h, a):
    for i in range(0, len(h)):
        url = 'https://wwwapi.kugou.com/yy/index.php?r=play/getdata&hash={}&album_id={}'.format(h[i], a[i])
        data = session.get(url, headers=headers, verify=False).json()
        address = data['data']['play_url']
        name = data['data']['audio_name']
        print(url)
        get_music(address, name)

def get_music(address, name):
    res = requests.get(address)
    music = res.content
    with open('酷狗音乐/{}.mp3'.format(name), 'ab') as file:  # 保存到本地的文件名
        file.write(music)
        file.flush()
    print('下载成功！' + name)
if __name__ == '__main__':
    session = requests.session()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36',
        'cookie': 'kg_mid=e33dbdb7757ebb113e03d5d058df4387; kg_dfid=3KxIs60QGOKi3Y1b413mUiDZ; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1619000429,1619002487; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1619015004'
    }
    h, a = get_hash_album()
    get_json(h, a)

