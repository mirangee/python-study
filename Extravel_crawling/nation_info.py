import json
import mysql.connector

# JSON 파일 읽기
with open('data.json', 'r') as f:
    data = json.load(f)

nation_code = data['cca2']
name = data['age']
flag = data['city']

# MySQL 데이터베이스 연결
cnx = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='mysql',
    database = 'jpa'
)

# SQL INSERT 명령 실행
cursor = cnx.cursor()
query = 'INSERT INTO tbl_nation VALUES(%s, %s, %s)'
values = (nation_code, name, flag)
cursor.execute(query, values)

cnx.commit()
cursor.close()
cnx.close()