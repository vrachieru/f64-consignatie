#!/usr/bin/env python

from f64 import Product
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

  def productExists(self, productCode):
    return (True, False)[self.getProduct(productCode) == None]

  def getProduct(self, productCode):
    for item in self._data:
      if item['code'] == productCode:
        price = self.getLatestPrice(item['price'])
        return Product(item['code'], item['title'], price, item['url'])
    return None

  def addProduct(self, product):
    self._data.append({ 'code' : product.code, 'title' : product.title, 
      'price' : { now() : product.price }, 'url' : product.url})

  def addPrice(self, productCode, newPrice):
    for item in self._data:
      if item['code'] == productCode:
        item['price'].update({ now() : newPrice })

  def getLatestPrice(self, prices):
    return sorted(prices.items())[-1][1]
