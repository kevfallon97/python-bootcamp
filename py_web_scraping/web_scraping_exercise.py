
# import required packages
import requests
import bs4

# Quotes to scrapte site url
base_url = "http://quotes.toscrape.com/page/{}/"

# # Get response
# res = requests.get(site_url)
# # Create soup
# soup = bs4.BeautifulSoup(res.text, 'lxml')

# # Get the names of all the authors on the first page

# #for author in soup.select(".author"):
# #	authors.add(author.text)

# # Create a list of all the quotes on the first page
# quotes = []
# for quote in soup.select(".text"):
# 	quotes.append(quote.text)

# # Get the top ten quotes on the page
# top_ten = []
# for item in soup.select(".tag-item"):
# 	top_ten.append(item.text)

# Get all the author names across all of the pages
authors = set()
n = 1
while True:
	scrape_url = base_url.format(n)
	res = requests.get(scrape_url)
	soup = bs4.BeautifulSoup(res.text, 'lxml')

	# add unique authors on every page
	for author in soup.select(".author"):
		authors.add(author.text)
	
	# if the last page is reached, break from the while loop
	if len(soup.select(".next")) != 0:
		n += 1
	else:
		break
print(authors)
