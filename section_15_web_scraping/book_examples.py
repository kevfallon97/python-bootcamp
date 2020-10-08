
# Goal is to get the title of every book with a two star rating

import requests
import bs4

base_url = "http://books.toscrape.com/catalogue/page-{}.html"
two_star_titles = []

# run through pages 1 to 50
for n in range(1,51):

	# scrape that particular page
	scrape_url = base_url.format(n)
	# make a request
	res = requests.get(scrape_url)
	# convert it to a soup 
	soup = bs4.BeautifulSoup(res.text, 'lxml')
	# search for all the product pods or books
	books = soup.select(".product_pod")
	# for each book check if it is two star rated and if so, append it to the list
	for book in books:
		if len(book.select(".star-rating.Two")) != 0:
			book_title = book.select("a")[1]["title"]
			two_star_titles.append(book_title)

for counter, title in enumerate(two_star_titles):
	print(f"Book {counter}: {title}")