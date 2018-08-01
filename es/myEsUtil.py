# -*- coding: utf-8 -*-
import json
import os
import sys
import time
import urllib2

reload(sys)
sys.setdefaultencoding('utf-8') 


class ExportEsData(object):
	size = 10000

	def __init__(self, url, index, type, target_index, begin_time, end_time):
		self.url = url + "/" + index + "/" + type + "/_search"

		self.data = {
			"sort": {
			    "article_publish_time": {
			      "order": "desc"
			    }
			},
			"query": {
				"bool": {
					"must": [
						{"range": { "article_publish_time": {"gte": "%s" % begin_time,"lte": "%s" % end_time} }}
					]
				}
			}
		}

		print "data: ", self.data

		self.request = urllib2.Request(self.url, headers={'Content-Type': 'application/json'}, data=json.dumps(self.data))


		self.index = index
		self.type = type
		self.target_index = target_index  # 替换原有的index
		self.file_name = self.target_index + "_" + self.type + ".json"

	def exportData(self):
		print("export data begin...\n")
		print self.url
		begin = time.time()
		try:
			os.remove(self.file_name)
		except:
			os.mknod(self.file_name)
		print (self.url)
		msg = urllib2.urlopen(self.url).read()
		print(msg)
		obj = json.loads(msg)
		num = obj["hits"]["total"]
		start = 0
		end = num / self.size + 1
		while start < end:
			tmpData = self.data
			tmpData["from"] = start * self.size
			tmpData["size"] = self.size
			request = urllib2.Request(self.url, headers={'Content-Type': 'application/json'}, data=json.dumps(tmpData))
			# msg = urllib2.urlopen(self.request + "?from=" + str(start * self.size) + "&size=" + str(self.size)).read()
			msg = urllib2.urlopen(request).read()
			self.writeFile(msg)
			start += 1
		print("export data end!!!\n total consuming time:" + str(time.time() - begin) + "s")

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
				f.write(m + "\n")
				f.write(v + "\n")
		finally:
			f.flush()
			f.close()


class ImportEsData(object):
	def __init__(self, url, index, type):
		self.url = "%s/%s/%s" % (url, index, type) 
		self.index = index
		self.type = type
		self.file_name = self.index + "_" + self.type + ".json"

	def importData(self):
		print("import data begin...\n")
		begin = time.time()
		print self.url
		try:
			# s = os.path.getsize(self.file_name)
			# f = open(self.file_name, "r")
			# data = f.read(s)
			# # 此处有坑: 注意bulk操作需要的格式(以\n换行)
			# self.post(data)
			f = open(self.file_name, "r")
			for line in f:
				self.post(line)

		finally:
			f.close()
		print("import data end!!!\n total consuming time:" + str(time.time() - begin) + "s")

	def post(self, data):
		# print data
		print self.url
		req = urllib2.Request(self.url, headers={'Content-Type': 'application/json', charset=UTF-8}, data=json.dumps(data))
		r = urllib2.urlopen(req)
		response = r.read()
		print response
		r.close()


if __name__ == '__main__':
	ExportEsData("http://10.9.134.113:9200", "smzdm_article_index_v9", "article", "smzdm_article_index_test", "2017-03-01 19:42:00", "2017-05-01 00:00:00").exportData()

	# ImportEsData("http://10.9.134.113:920/_bulk", "smzdm_article_index_test", "article").importData()
