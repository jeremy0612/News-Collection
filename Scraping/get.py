from bs4 import BeautifulSoup
import requests

def GetAuthor(soup):
	author_elem = soup.find('div', class_='author-byline').find('a')
	author = author_elem.text.strip() if author_elem else ''
	return author

def GetTopic(soup):
	topic = soup.find('div', class_= 'eyebrow').find('a').text
	return topic

def GetDatePublish(soup):
	date_pulished = soup.find('time').text
	return date_pulished
def  GetTitle(soup):
	title = soup.find('h3', class_='title').text.strip() 
	return title
def GetLink(soup):
	link_elem = soup.find('a')
	link = link_elem['href'] if link_elem else ''
	return link

if __name__ == '__main__':
	main()