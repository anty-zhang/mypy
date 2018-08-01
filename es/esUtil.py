# -*- coding: utf-8 -*-
import json
import os
import sys
import time
import urllib2
from elasticsearch import Elasticsearch

reload(sys)
sys.setdefaultencoding('utf-8')  # @UndefinedVariable

"""
http://www.voidcn.com/blog/lein_wang/article/p-6087708.html
"""


class ExportEsData(object):
	size = 10000

	def __init__(self, url, index, type, target_index, begin_time, end_time):
		# self.url = url + "/" + index + "/" + type + "/_search? -d "
		self.url = """%s/%s/%s/_search?pretty -d '{"query" : {
										"bool": {
											"must": [
									            { "range": { "ctime": {"gte": "%s","lte": "%s"} }}
											]
									    }
									}}'""" % (url, index, type, begin_time, end_time)
		self.index = index
		self.type = type
		self.target_index = target_index  # 替换原有的index
		self.file_name = self.target_index + "_" + self.type + ".json"

		self.es = Elasticsearch(
			hosts=[{'host': 'localhost', 'port': 9200}],
			http_auth=('xiaoqiang', 'xxx'),
		)

	def exportData(self):
		print("export data begin...\n")
		print self.url
		begin = time.time()
		try:
			os.remove(self.file_name)
		except:
			os.mknod(self.file_name)
		# print (self.url)
		# msg = urllib2.urlopen(self.url).read()
		res = self.es.search(index="recommend", doc_type="association_rule", body={"query": {
			"bool": {
				"must": [
					{"range": {"ctime": {"gte": "2016-09-18 00:00:00", "lte": "2016-09-19 00:00:00"}}},
				]
			}
		}
		})
		print res
		# print(msg)
		# obj = json.loads(msg)
		# num = obj["hits"]["total"]
		# start = 0
		# end = num / self.size + 1
		# while start < end:
		# 	msg = urllib2.urlopen(self.url + "?from=" + str(start * self.size) + "&size=" + str(self.size)).read()
		# 	self.writeFile(msg)
		# 	start += 1
		# print("export data end!!!\n total consuming time:" + str(time.time() - begin) + "s")

	def writeFile(self, msg):
		obj = json.loads(msg)
		vals = obj["hits"]["hits"]
		try:
			f = open(self.file_name, "a")
			for val in vals:
				# prepare for bulk insert，注意格式
				meta_json = {"index": {"_index": self.target_index, "_type": val["_type"], "_id": val["_id"]}}
				val_json = val["_source"]
				val_json["ori"] = 1
				val_json["mall"] = u"-1"
				m = json.dumps(meta_json, ensure_ascii=False)
				v = json.dumps(val_json, ensure_ascii=False)
				print ("zhanggq test: ", v)
				f.write(m + "\n")
				f.write(v + "\n")
		finally:
			f.flush()
			f.close()


class ImportEsData(object):
	def __init__(self, url, index, type):
		self.url = url
		self.index = index
		self.type = type
		self.file_name = self.index + "_" + self.type + ".json"

	def importData(self):
		print("import data begin...\n")
		begin = time.time()
		print self.url
		try:
			s = os.path.getsize(self.file_name)
			f = open(self.file_name, "r")
			data = f.read(s)
			# 此处有坑: 注意bulk操作需要的格式(以\n换行)
			self.post(data)

		finally:
			f.close()
		print("import data end!!!\n total consuming time:" + str(time.time() - begin) + "s")

	def post(self, data):
		print data
		print self.url
		req = urllib2.Request(self.url, data)
		r = urllib2.urlopen(req)
		response = r.read()
		print response
		r.close()


if __name__ == '__main__':
	'''
		Export Data
		e.g.
							URL                    index        type
		exportEsData("http://10.100.142.60:9200","watchdog","mexception").exportData()

		export file name: watchdog_mexception.json
	'''
	# exportEsData("http://10.100.142.60:9200","watchdog","mexception").exportData()
	# exportEsData("http://127.0.0.1:9200", "forum", "CHAT", "chat").exportData()
	# exportEsData("http://127.0.0.1:9200", "forum", "TOPIC", "chat").exportData()

	# '''
	# 	Import Data
	#
	# 	*import file name:watchdog_test.json    (important)
	# 				"_" front part represents the elasticsearch index
	# 				"_" after part represents the  elasticsearch type
	# 	e.g.
	# 						URL                    index        type
	# 	mportEsData("http://10.100.142.60:9200","watchdog","test").importData()
	# '''
	# # importEsData("http://10.100.142.60:9200","watchdog","test").importData()
	# importEsData("http://127.0.0.1:9200/_bulk", "chat", "CHAT").importData()
	# importEsData("http://127.0.0.1:9200/_bulk", "chat", "TOPIC").importData()
	# ExportEsData("http://127.0.0.1:9200", "song001", "list001", "song001_test", "2016-09-19 00:00:00", "2016-09-21 00:00:00").exportData()
	ExportEsData("http://127.0.0.1:9200", "recommend", "association_rule", "recommend_1", "2016-09-19 00:00:00", "2016-09-21 00:00:00").exportData()
	# ImportEsData("http://127.0.0.1:9200/_bulk", "song001_test", "list001").importData()

	'''
		python esUtil.py "http://127.0.0.1:9200"   "recommend"   "association_rule" "2016-09-19 00:00:00" "2016-09-21 00:00:00" "http://127.0.0.1:9200/_bulk" "recommend_v_1"
	'''

	# export_url = sys.argv[1]
	# export_index = sys.argv[2]
	# export_type = sys.argv[3]
	# export_begin_time = sys.argv[4]
	# export_end_time = sys.argv[5]
	#
	# import_url = sys.argv[6]
	# import_index = sys.argv[7]
	#
	# ExportEsData(export_url, export_index, export_type, import_index, export_begin_time, export_end_time).exportData()
	# ImportEsData(import_url, import_index, export_type).importData()



