from bs4 import BeautifulSoup
import requests

response= requests.get("https://news.ycombinator.com")
yc_web_page=response.text
soup=BeautifulSoup(yc_web_page,"html.parser")
articles=soup.find_all(name="a",class_="storylink")
article_texts=[];
article_links=[]
for article_tag in articles:
	article_text=article_tag.getText()
	article_texts.append(article_text)
	article_link=article_tag.get("href")
	article_links.append(article_link)
article_upvotes=[score.getText().split()[0] for score in soup.find_all(name="span",class_="score")]

# print(article_upvotes)
print(article_upvotes)

# import lxml

# with open("website.html") as file:
# 	contents= file.read()

# soup= BeautifulSoup(contents,'html.parser')

# all_Anchor_tags=soup.find_all(name="a")

# for tag in all_Anchor_tags:
# 	print(tag.get("href"))

# heading=soup.find(name="h1",id="name")
# print(heading)

