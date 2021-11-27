# -*- coding:UTF-8 -*-
import requests
import sqlite3

# conn = sqlite3.connect('car.sqlite')
# print("Opened database successfully")
# c = conn.cursor()
# c.execute('''CREATE TABLE car
#        (ID INT PRIMARY KEY     NOT NULL,
#        NAME           TEXT    NOT NULL,
#        AGE            INT     NOT NULL,
#        ADDRESS        CHAR(50),
#        SALARY         REAL);''')
# print("Table created successfully")
# conn.commit()
# conn.close()

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
}
data = {
    'offset':'0',
    'limit':'30',
    'is_refresh':'0',
    # 'city_name':'深圳',
    'price':'15,60'
}
def one():
    url = 'https://www.dcdapp.com/motor/brand/m/v1/select/series/?city_name=%E6%B7%B1%E5%9C%B3'
    try:
        response = requests.post(url, headers=headers,data=data)
        if response.status_code == 200:
            res = response.json()
            for i in range(0, len(res['data']['series'])):
                print(res['data']['series'][i]['outter_name'])
            return response.json()
    except requests.ConnectionError as e:
        print('Error', e.args)

if __name__ == '__main__':
    one()