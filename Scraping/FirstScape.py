
"""This code is used to scrape data from Fox News"""

from bs4 import BeautifulSoup
import requests
import get # file get.py has funcitons, that reduce code length

def GetPost(link):
	paragraph_html_text = requests.get(link)
	paragraph_soup = BeautifulSoup(paragraph_html_text.text, 'lxml')

	date_published = get.GetDatePublish(paragraph_soup)
	author = get.GetAuthor(paragraph_soup)
	topic = get.GetTopic(paragraph_soup)

	"""print(author)
				print(date_publish)
				print(topic)"""
	paragraphs = paragraph_soup.find_all('p')
	contents = "!!!CONTENTS OF POST IS HERE!!!\n"
	for paragraph in paragraphs:
		paragraph = paragraph.text
		contents = contents + paragraph + '\n'
	return [author+'\n', date_published+'\n', topic+'\n', contents+'\n']

html_text = requests.get("https://www.foxnews.com/").text
soup = BeautifulSoup(html_text, 'lxml')

posts = soup.find_all("article", class_='article story-1')

for post in posts:
	try:
		title = get.GetTitle(post)
		link = get.GetLink(post)
		#link= 'https://www.foxnews.com/politics/biden-sanctions-russia-iran-wrongful-detention-hostage-taking-release-immediately'
		#print(link)
		All_item = [title+'\n', link+'\n'] + GetPost(link)
		with open("example.txt",'w+') as file:
			for i in All_item:
				file.write(i)
	except:
		continue
	#print(All_item)
	#break #For test, we just need to scrape one

#    if(tille != None):
#	    print(tille)
#	    print(link)