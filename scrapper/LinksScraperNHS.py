import os
import re

from bs4 import BeautifulSoup

import requests

"""
This class scrapes and makes individual pdf of each health condition given in 'https://www.nhs.uk/conditions/'

The most relevant method in this class is the scrapeEachConditions and this should be called when using this class.
"""
class LinksScraperNHS:

    """
    initialises the class
    """
    def __init__(self, main_url = 'https://www.nhs.uk/conditions/'):
        self.main_url = main_url

    """
    Scrapes each health conditions and makes a pdf out of it.
    
    :param main_url: main url
    :param directory: directory to save the pdf to
    """
    def scrapeEachConditions(self, main_url, directory = './ScrappedPDFs/'):
        # getting the health conditions from getLinks Method
        conditions = self.getLinks(main_url)

        totalConditions = len(conditions)
        conditionNumber = 1

        # loop running though each conditions
        for condition in conditions:
            # getting to health condition page through requests
            conditionPage = requests.get(condition)

            # making a soup of the condition page for scraping
            conditionSoup = BeautifulSoup(conditionPage.text, 'html.parser')

            # extracting title for filename
            fileName = conditionSoup.find('title').get_text()
            fileName = fileName.split(' - NHS')[0]
            fileName = fileName.replace(" ", "")
            fileName = str(conditionNumber) + fileName

            # extracting text for pdf content
            text = conditionSoup.get_text(" ", strip=True)

            # calls the textToPDF method to save the text as a pdf
            # self.textToPDF(text, fileName, directory)
            self.textToFile(text, fileName, directory)

            print("Saved condition " + str(conditionNumber) + " out of " + str(totalConditions))
            conditionNumber += 1


    """
    Scrapes the sub urls from the main url
    
    :param main_url: main url that leads us to the nhs website with links to different conditions.
    """
    def getLinks(self, main_url):
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
        return links

    """
    method to convert text to File
    :param text: text to convert
    :param directory: directory to save the pdf to
    :param fileName: name of the pdf file
    """
    def textToFile(self, text, fileName, directory):
        # Sanitize the file name by removing or replacing invalid characters
        sanitized_file_name = re.sub(r'[\\/*?:"<>|]', "_", fileName.strip())  # Replace invalid chars with '_'
        sanitized_file_name = sanitized_file_name.replace("\n", "").replace("\r", "")  # Remove newlines

        # Ensure the directory exists, create it if necessary
        if not os.path.exists(directory):
            os.makedirs(directory)

        # Create an individualized file path
        file_path = os.path.join(directory, f"{sanitized_file_name}.txt")

        # Write the text to the file
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(text)


    """
    def textToPDF(self, text, fileName, directory):
        # Sanitize filename
        sanitized_file_name = re.sub(r'[\\/*?:"<>|]', "_", fileName.strip())
        sanitized_file_name = sanitized_file_name.replace("\n", "").replace("\r", "")

        # Ensure directory exists
        if not os.path.exists(directory):
            os.makedirs(directory)

        # Create file path
        file_path = os.path.join(directory, f"{sanitized_file_name}.pdf")

        # Create PDF object
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=11)

        # Set margins (in mm)
        pdf.set_margins(20, 20, 20)

        # Split text into smaller chunks to handle encoding issues
        # and add line breaks for readability
        chunks = text.split('. ')

        # Write text to PDF
        for chunk in chunks:
            if chunk.strip():  # Only process non-empty chunks
                # Add a period back if it's not the last chunk
                chunk = chunk.strip() + '. '
                # Encode and decode to handle special characters
                try:
                    # Use multi_cell for automatic text wrapping
                    pdf.multi_cell(0, 8, chunk)
                    pdf.ln(2)  # Add a small space between paragraphs
                except Exception as e:
                    # If there's an encoding error, try to clean the text
                    cleaned_chunk = chunk.encode('ascii', 'replace').decode()
                    pdf.multi_cell(0, 8, cleaned_chunk)
                    pdf.ln(2)

        # Save the PDF
        try:
            pdf.output(str(file_path))
        except Exception as e:
            print(f"Error saving PDF {fileName}: {str(e)}")

    
    method to convert text to PDF and save it.

    :param text: text to convert
    :param directory: directory to save the pdf to
    :param fileName: name of the pdf file
    """
    """
    def textToPDF(self, text, fileName, directory):

        # Remove BOM and non-ASCII characters
        #text = text.replace('\ufeff', '').encode('latin-1', 'replace').decode('latin-1')

        # Sanitize the file name by removing or replacing invalid characters
        sanitized_file_name = re.sub(r'[\\/*?:"<>|]', "_", fileName.strip())  # Replace invalid chars with '_'
        sanitized_file_name = sanitized_file_name.replace("\n", " ").replace("\r", "")  # Remove newlines

        # Ensure the directory exists, create it if necessary
        if not os.path.exists(directory):
            os.makedirs(directory)

        # create a individualised filepath
        file_path = os.path.join(directory, f"{sanitized_file_name}.pdf")

        # Create a PDF object
        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        # Add text to the PDF
        pdf.multi_cell(0, 10, text)

        # Save the PDF
        pdf.output(str(file_path))


    def textToPDF(self, text, fileName, directory):
        # Sanitize the file name by removing or replacing invalid characters
        sanitized_file_name = re.sub(r'[\\/*?:"<>|]', "_", fileName.strip())  # Replace invalid chars with '_'
        sanitized_file_name = sanitized_file_name.replace("\n", " ").replace("\r", "")  # Remove newlines

        # Ensure the directory exists, create it if necessary
        if not os.path.exists(directory):
            os.makedirs(directory)

        # Create an individualized file path
        file_path = os.path.join(directory, f"{sanitized_file_name}.pdf")

        # Create a ReportLab canvas object
        c = canvas.Canvas(str(file_path), pagesize=letter)

        # Set font to Times New Roman
        c.setFont("Times-Roman", 12)

        # Define the starting position
        x = 40
        y = 750

        # Set the text width (line width)
        width = 520  # You can adjust this value depending on how much space you want for the text

        # Create the text object for multi-line text
        text_object = c.beginText(x, y)
        text_object.setFont("Times-Roman", 12)
        text_object.setTextOrigin(x, y)

        # Wrap the text to fit within the specified width
        from reportlab.lib.pagesizes import letter
        text_object.setTextOrigin(x, y)

        # Split the text into lines that fit within the width of the page
        from reportlab.lib import pagesizes
        text_object.setTextOrigin(x, y)
        text_object.setFont("Times-Roman", 12)

        # Use `wrap` method for automatic text wrapping within the width of the page
        lines = c.beginText(40, 750)
        lines.setFont("Times-Roman", 12)
        lines.setTextOrigin(40, 750)
        lines.textLines(text)

        # Draw the text onto the PDF
        c.drawText(lines)

        # Save the PDF
        c.save()
        """
