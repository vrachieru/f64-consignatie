#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from configuration import Configuration
from twitter import Twitter
from database import Database
from f64 import F64
from logger import Logger

TAGS     = "#f64"

log      = Logger()
config   = Configuration()
database = Database()
f64      = F64()
twitter  = Twitter(config.twitter)

def addProduct(product):
	database.addProduct(product)
	twitter.tweet("%s @ %s %s %s" %
		(product.title, product.price, product.url, TAGS))
	log.write("%s @ %s" %
		(product.title, product.price))

def updateProduct(product, oldPrice):
	database.addPrice(product.code, product.price)
	symbol = (u"↗", u"↘")[oldPrice > product.price]
	twitter.tweet("%s @ %s %s %s %s %s" %
		(product.title, oldPrice, symbol, product.price, product.url, TAGS))
	log.write("%s @ %s %s %s" %
		(product.title, oldPrice, symbol, product.price))

def main():
	for product in f64.products:
		if not database.productExists(product.code):
			addProduct(product)
		else:
			oldPrice = database.getProduct(product.code).price
			if oldPrice != product.price:
				updateProduct(product, oldPrice)
	database.write()

main()
