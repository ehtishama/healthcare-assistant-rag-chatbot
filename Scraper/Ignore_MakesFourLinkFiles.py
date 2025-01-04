from LinksScraperNHS import LinksScraperNHS

scraper = LinksScraperNHS()

links = scraper.getLinks(scraper.main_url)

text = ''
count = 0
last = len(links)-1
for link in links:
    linktext = link
    if count==300 or count == 600 or count == 900 or count == last:
        # convert text to a text file and store it in scraper
        scraper.textToFile(text, str(count) + "links.txt", './Ignore_JustLinks/')
        text = ''
    text = text + linktext + "\n"
    count = count + 1