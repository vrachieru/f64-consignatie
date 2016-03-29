#!/usr/bin/env python

from lxml import html
from requests import get

BASE_URL = "http://www.f64.ro"
PER_PAGE = 1000
CATEGORIES = [
	"aparate-foto-second-hand",
	"obiective-foto-second-hand",
	"blitz-uri-lumini-studio-accesorii-second-hand"
]

class F64():
	products = []

	def __init__(self):
		map(self.parse, CATEGORIES)

	def parse(self, category):
		url = self.getCategoryUrl(category)
		content = self.getPageContent(url)
		products = self.parseProducts(content)
		map(lambda p : self.products.append(self.parseProduct(p)), products)

	def getCategoryUrl(self, category):
		return "%s/%s.html?per_page=%s" % (BASE_URL, category, PER_PAGE)

	def getPageContent(self, url):
		return html.fromstring(get(url).content)

	def parseProducts(self, dom):
		return dom.xpath('//div[@class="product_list_container"]')

	def parseProduct(self, product):
		title = self.parseProductTitle(product)
		code = self.parseProductCode(product)
		price = self.parseProductPrice(product)
		url = self.parseProductUrl(product)
		return Product(title, code, price, url)

	def parseProductUrl(self, product):
		return product.xpath('.//td[@class="product_title"]//a/@href')[0]

	def parseProductTitle(self, product):
		return product.xpath('.//h2/text()')[0]

	def parseProductCode(self, product):
		return product.xpath('.//div[@class="stars_cod_product"]//b/text()')[0]

	def parseProductPrice(self, product):
		return product.xpath('.//span[@class="price_list_int"]/text()')[0] + "," + product.xpath('.//sup[@class="price_list_dec"]/text()')[0] + " " + product.xpath('.//span[@class="price_list_currency"]/text()')[0]


class Product():
	def __init__(self, title, code, price, url):
		self.title = title
		self.code = code
		self.price = price
		self.url = url