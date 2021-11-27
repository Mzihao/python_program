# -*- coding:UTF-8 -*-
import requests
from pyquery import PyQuery as pq


class Login(object):
    def __init__(self):
        self.headers = {
            'Referer': 'https://github.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
            'Host': 'github.com'
        }
        self.login_url = 'https://github.com/login'
        self.post_url = 'https://github.com/session'
        self.feed_url = 'https://github.com/dashboard-feed'
        self.logined_url = 'https://github.com/settings/profile'
        ## 维持会话，自动处理cookies
        self.session = requests.Session()

    ## 解析出登录所需要的
    def token(self):
        response = self.session.get(self.login_url, headers=self.headers)
        selector = pq(response.text)
        token = selector('input[name="authenticity_token"]').attr('value')
        return token

    def login(self, email, password):
        # print(self.token())
        post_data = {
            'commit': 'Sign in',
            'utf8': '✓',
            'authenticity_token': self.token(),
            'login': email,
            'password': password
        }
        response = self.session.post(self.post_url, data=post_data, headers=self.headers)
        if response.status_code == 200:
            # self.dynamics(response.text)
            print(response.text)
        response = self.session.get(self.logined_url, headers=self.headers)
        #if response.status_code == 200:
            # self.profile(response.text)

if __name__ == "__main__":
    login = Login()
    login.login(email='Mzihao', password='mzh19980112')