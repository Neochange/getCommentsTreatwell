from lxml import html
import requests

i=1
page = requests.get('https://www.treatwell.es/establecimiento/estetic-natura/reviews/pagina-' + str(i) + "/")
while i < 20:
	tree = html.fromstring(page.content)

	# get all comments of page 1
	comments_text = tree.xpath('//div[@itemprop="reviewBody"]/text()')

	for comment in comments_text:
		print(str(comment))

	i=i+1
	page = requests.get('https://www.treatwell.es/establecimiento/estetic-natura/reviews/pagina-' + str(i) + "/")
