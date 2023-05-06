import requests
from lxml import html
from bs4 import BeautifulSoup
import json
import csv
url = 'https://www.foxnews.com/politics/kennedy-stumps-biden-official-fifty-trillion-price-tag-climate-change'
response = requests.get(url)
tree = html.fromstring(response.content)

def GetLink(tree):
	#link = tree.xpath('//script[@type="application/ld+json"]/text()')[0]
	link_url = tree.xpath('//script[@type="application/ld+json"]/text()')[0].split('"mainEntityOfPage": "')[1].split('",')[0]
	#print(link_url)
	return link_url
def GetTitle(tree):
	#Title = tree.xpath('//script[@type="application/ld+json"]/text()')[0]
	Title = tree.xpath('//script[@type="application/ld+json"]/text()')[0].split('"headline": "')[1].split('",')[0]
	#print(Title)
	return Title 
def GetAuthor(tree):
	author = tree.xpath('//script[@type="application/ld+json"]/text()')[0]
	json_data = json.loads(author)
	author_name = json_data['author'][0]['name']
	author_url = json_data['author'][0]['url']
	return [author_name, author_url]
def GetContent(tree):
	Content = tree.xpath('//script[@type="application/ld+json"]/text()')[0].split('"articleBody": "')[1].split('",')[0]
	#print(Content)
	return Content.replace('&apos;', "'").replace('&quot;', '"').replace('&gt;', '>').replace('&lt;', '<').replace('&amp;', '&').replace('&#xA0;', '').replace('\\','')
def GetDatePublished(tree):
	Date = tree.xpath('//script[@type="application/ld+json"]/text()')[0].split('"datePublished": "')[1].split('",')[0]
	return Date

link = GetLink(tree)
Title = GetTitle(tree)
Author = GetAuthor(tree)[0]
Author_url = GetAuthor(tree)[1]
Content = GetContent(tree)
DatePublished = GetDatePublished(tree)

All_items = [link, Title, Author, Author_url, DatePublished,'', Content ]

with open('ex.csv','w',newline='') as ex:
	TrackPost = csv.writer(ex)
	TrackPost.writerow(['Link', 'Title', 'Author', 'Link Author', 'Date Published', 'Topic', "Content" ])
	TrackPost.writerow((All_items))
"""with open('exa.docs','w+') as ex:
	ex.write(Content)"""