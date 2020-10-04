# REQUIRED PACKAGES
# pip install requests
# pip install lxml
# pip install bs4

import requests
import bs4

# EXAMPLE TASK 0 - GRABBING A PAGE TITLE

# Use the requests library to grab the page, returns a reponse
result = requests.get("http://www.example.com")

# Use bs4 to parse the result.text, creates a easy to read soup object
soup = bs4.BeautifulSoup(result.text,"lxml")

# Grab the page title using the .select method
# .select will return a list of the matching tags
# get the first title tag and convert it to text
title = soup.select("title")[0].getText()
print(f"Page title: {title}")

# EXAMPLE TASK 1 - GRABBING ALL ELEMENTS OF A CLASS

res = requests.get("https://en.wikipedia.org/wiki/Patrick_Bateman")
soup = bs4.BeautifulSoup(res.text, "lxml")

for item in soup.select(".toctext"):
	print(item.text)

# EXAMPLE TASK 2 - GRABBING AN IMAGE

bateman = soup.select("img")[0]
image_link = requests.get("https://upload.wikimedia.org/wikipedia/en/thumb/5/52/American-psycho-patrick-bateman.jpg/220px-American-psycho-patrick-bateman.jpg")

# wb -> write binary
f = open("bateman_img.jpg", "wb")
f.write(image_link.content)
f.close()