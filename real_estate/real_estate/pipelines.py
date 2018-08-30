# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem
import psycopg2

class ValidatePipeline(object):
	def __init__(self):
		self.ids_seen = set()

	def process_item(self, item, spider):
		if item in self.ids_seen:
			raise DropItem("Duplicate item found:")
		else:
			self.ids_seen.add(item)
			return item


class RealEstatePipeline(object):
    def __init__(self):
    	self.connection = psycopg2.connect(host="localhost", database="mydb", user="postgres", password='bang1511', port=5433)
    	self.cur = self.connection.cursor()

    def process_item(self, item, spider):
    	self.cur.execute("insert into real_estate(title, price, contact, name_contact, detail, area, address, number_bedroom) values(%s,%s,%s,%s,%s,%s,%s,%s)",(item['title'],item['price'],item['contact'],item['name_contact'],item['detail'],item['area'],item['address'],item['number_bed_room']));
    	self.connection.commit()
    	return item