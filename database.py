#!/usr/bin/env python

from json import load, dumps
from os.path import isfile
from utils import now

databaseFile = 'database.json'

class Database():
	_data = [];

	def __init__(self):
		self._data = self.readOrCreate()

	def readOrCreate(self):
		if not isfile(databaseFile):
			self.create()
			return []
		with open(databaseFile, 'r') as data:
			return load(data)

	def create(self):
		with open(databaseFile, 'w+') as data:
			data.write("[]")

	def write(self):
		with open(databaseFile, 'w+') as data:
			data.write(dumps(self._data, sort_keys=True, indent=4))

	def productExists(self, product):
		return (True, False)[self.getProduct(product) == None]

	def getProduct(self, product):
		for item in self._data:
			if item['product'] == product:
				return item
		return None

	def addProduct(self, code, title, price, url):
		self._data.append({ 'product' : code, 'title' : title, 'price' : { now() : price }, 'url' : url})

	def updatePrice(self, product, title, price, url):
		latestPrice = self.getLatestPrice(product)
		if latestPrice != price:
			self.addNewPrice(product, price)

	def getLatestPrice(self, product):
		return sorted(self.getProduct(product)['price'].items())[-1][1]

	def addNewPrice(self, product, price):
		self.getProduct(product)['price'].update({ now() : price })
