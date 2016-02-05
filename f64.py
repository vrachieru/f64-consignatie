from time import gmtime, strftime
from lxml import html
import requests
import json

categories = {
	"lenses" : "http://www.f64.ro/obiective-foto-second-hand.html?Montura[]=Nikon", 
	"accessories" : "http://www.f64.ro/blitz-uri-lumini-studio-accesorii-second-hand.html"
}

class Html():
	@staticmethod
	def read(url):
		return html.fromstring(requests.get(url).content)


class Category():
	@staticmethod
	def displayProducts(products):
		for product in products:
			print Category.getProduct(product)

	@staticmethod
	def getProducts(dom):
		return dom.xpath('//div[@class="product_list_container"]')

	@staticmethod
	def getProduct(product):
		return { 'product' : Category.getProductCode(product), 'title' : Category.getTitle(product), 'price' : Category.getPrice(product) }
	
	@staticmethod
	def getTitle(product):
		return product.xpath('.//h2/text()')[0]

	@staticmethod
	def getProductCode(product):
		return product.xpath('.//div[@class="stars_cod_product"]//b/text()')[0]

	@staticmethod
	def getPrice(product):
		return product.xpath('.//span[@class="price_list_int"]/text()')[0] + "," + product.xpath('.//sup[@class="price_list_dec"]/text()')[0] + " " + product.xpath('.//span[@class="price_list_currency"]/text()')[0]


class Log():
	@staticmethod
	def write(data):
		with open("f64.log", "a") as f:
			f.write(strftime('%Y-%m-%d %H:%M:%S', gmtime()) + " : " + data + "\n")


class Database():
	data = [];

	def __init__(self):
		self.read()

	def read(self):
		with open('f64.db', 'r') as f:
			self.data = json.load(f)

	def write(self):
		with open('f64.db', 'w') as f:
			f.write(json.dumps(self.data, sort_keys=True, indent=2))

	def productExists(self, product):
		return (True, False)[self.getProduct(product) == None]

	def getProduct(self, product):
		for item in self.data:
			if item['product'] == product:
				return item
		return None

	def addProduct(self, code, title, price):
		self.data.append({ 'product' : code, 'title' : title, 'price' : { strftime('%Y-%m-%d %H:%M:%S', gmtime()) : price }})
		Log.write("New product [" + code + "] " + title + " @ " + price)

	def updatePrice(self, product, price):
		if self.getLatestPrice(product) != price:
			self.addNewPrice(product, price)
			Log.write(product + " price updated from " + self.getLatestPrice(product) + " to " + price)

	def getLatestPrice(self, product):
		return sorted(self.getProduct(product)['price'].items())[-1][1]

	def addNewPrice(self, product, price):
		self.getProduct(product)['price'].update({ strftime('%Y-%m-%d %H:%M:%S', gmtime()) : price })


def main():
	database = Database()

	for name, url in categories.items():
		products = Category.getProducts(Html.read(url))
		for product in products:
			p = Category.getProduct(product)
			if database.productExists(p['product']) == False:
				database.addProduct(p['product'], p['title'], p['price'])
			else:
				database.updatePrice(p['product'], p['price'])

	database.write()

main()