from datetime import datetime
from elasticsearch import Elasticsearch
import MySQLdb
es = Elasticsearch(
    hosts=[{'host': '106.75.50.101', 'port': 9200}],
    http_auth=('wanxin', 'tZjqlFsacs3AT5Th'),
)
db_host='smzdm_recommend_mysql_m01'
port='3306'
db_user='smzdm'
db_password='smzdm'
db_name='recommendDB'
db_conn = MySQLdb.connect(db_host,db_user,db_password,db_name, charset="utf8")
file_object = open('thefile3.txt', 'w')
sql_str = """select distinct device_id from recommend_hour_20160918_test
                 where article_channel_id = 1
                 and article_ctime >= '2016-09-16' 
                 and is_delete<>9
                 """
cursor=db_conn.cursor()
cursor.execute(sql_str)
result=cursor.fetchall()
count=0
for deviceid in result:
    #count=count+1
    deviceid=list(deviceid)[0].encode('utf8')
    res = es.count(index="recommend", body={"query": {
        "bool": {
          "must": [
            { "match": { "device_id": deviceid } },  ###鏌ヨ鏉′欢1
            { "match": { "article_channel_id": 1 } },          ###鏌ヨ鏉′欢2
            { "range": { "ctime": {"gte":"2016-09-18 00:00:00","lte":"2016-09-19 00:00:00"}} },
            { "range": { "article_ctime": {"gte":"2016-09-16 00:00:00","lte":"2016-09-19 00:00:00"}} }
          ],
          "must_not": [{"match": {"is_delete": 9}}]       
        }
      }
    })
    sql_count = """select count(*) from recommend_hour_20160918_test 
                 where device_id='{device_id}' and article_channel_id = 1
                 and article_ctime >= '2016-09-16 00:00:00' and  article_ctime <= "2016-09-19 00:00:00" 
                 and is_delete<>9
                 """.format(device_id=deviceid)
    cursor.execute(sql_count)
    count=cursor.fetchone()
    if res['count']==count:
        continue
    else:
        file_object.write(deviceid)
        file_object.write('\n')
    if count > 10:
        break
cursor.close()
db_conn.close()
file_object.close()