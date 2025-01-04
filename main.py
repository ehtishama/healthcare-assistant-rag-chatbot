# main.py

from Scraper.LinksScraperNHS import LinksScraperNHS

def main():
    # Initialize the scraper class
    scraper = LinksScraperNHS()

    # Call scrapeEachConditions with the main URL and the desired directory to save PDFs
    scraper.scrapeEachConditions(scraper.main_url, './ScrappedPDFs')

if __name__ == '__main__':
    main()