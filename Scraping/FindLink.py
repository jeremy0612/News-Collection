from bs4 import BeautifulSoup
import requests
import get # file get.py has funcitons, that reduce code length
import csv
from lxml import html
with open('Links.csv','a', newline = '') as file:
	TrackPost = csv.writer(file)

	url = 'https://www.foxnews.com/'
	html_text = requests.get(url).text
	soup = BeautifulSoup(html_text, 'lxml')
	links = soup.find_all("h3",class_='title')
	for link in links:
		try:
			a = link.find('a')
			link= a.get('href')
			title = a.text
			#print(title)
			TrackPost.writerow([link, title])
		except:
			continue

#link = tree.find_all('//article[@class="title"]/@href')[0]
# In ra liên kết
#print(link)"""