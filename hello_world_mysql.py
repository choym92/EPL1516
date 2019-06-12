import pymysql
conn = pymysql.connect(host = '127.0.0.1', user = 'root', passwd = 'Yusarang10101993!',db='bank')
cur = conn.cursor()
cur.execute("USE bank")
cur.execute("SELECT * FROM person WHERE id=1")
print(cur.fetchone())
cur.close()
conn.close()