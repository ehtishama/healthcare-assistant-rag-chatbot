"""This is a useless class just for test DO NOT USE IT"""


from bs4 import BeautifulSoup
import requests


main_url = 'https://www.nhs.uk/conditions/'


"""
Scrapes the sub urls from the main url

:param main_url: main url that leads us to the nhs website with links to different conditions.
"""

# this gets us to main page via requests
main_page = requests.get(main_url)

# creating soup of the main_page
soup = BeautifulSoup(main_page.text, 'html.parser')
# print(soup.prettify())

# find_all to get a html containing only the relevant links. links will be extracted from this
link_soup = soup.find_all('ul', class_='nhsuk-list nhsuk-list--border')
# print(link_soup)

# this scrapes all the 'a' tags
a_tags = soup.find_all('a', href=True, class_=None)
# print(a_tags)

# now we will extract the links and put them to an array Links
links = []
for a_tag in a_tags:
    links.append("https://www.nhs.uk" + a_tag['href'])

##########################
# for a condition
condition = links[1079]

subPage = requests.get(condition)

# creates a soup of the page
subSoup = BeautifulSoup(subPage.text, 'html.parser')
#print(subSoup.prettify())

title = subSoup.find('title').get_text()
title = title.split(' - NHS')[0]
title = title.replace(" ", "")
print(title)

# text = subSoup.get_text(" ", strip=True)
# print(text)
# print(type(text))

