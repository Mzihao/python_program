import sqlite3

conn = sqlite3.connect('car.sqlite')
print("Opened database successfully")
c = conn.cursor()
c.execute('''CREATE TABLE Car
       (ID INT PRIMARY KEY     NOT NULL,
       NAME           CHAR(50)    NOT NULL,
       count            INT     NOT NULL,
       rank            INT     NOT NULL,
       Min_price       FLOAT    NOT NULL,
       Max_price       FLOAT    NOT NULL,
       IMG_ADDRESS        CHAR(50)  not null);''')
print("Table created successfully")
conn.commit()
conn.close()