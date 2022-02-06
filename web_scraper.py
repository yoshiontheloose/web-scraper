from bs4 import BeautifulSoup
import requests


# Citation needed locations
#   - Before European arrival - Beginnings x1
#   - Major Civilizations - Aztec Empire x2
#   - Spanish Conquest - aftermath of the conquest x1
#   - spanish rule - evolution of race mixture x1


url = 'https://en.wikipedia.org/wiki/History_of_Mexico'

# Scrape a Wikipedia page and record which passages need citations.

def get_citations(url):
  page = requests.get(url)
  soup = BeautifulSoup(page.content, 'html.parser')
  titles = soup.findAll('a')
  return titles

# get_citations(url)

# Your web scraper should report the number of citations needed.
# Count function must be named get_citations_needed_count
# get_citations_needed takes in a url and returns an integer

# def get_citations_needed_count(url):




# Your web scraper should identify those cases AND include the relevant passage.
# E.g. Citation needed for “lorem spam and impsum eggs”
# Consider the “relevant passage” to be the parent element that contains the passage, often a paragraph element.

# Report function must be named get_citations_needed_report
# get_citations_needed_report takes in a url and returns a string
# the string should be formatted with each citation needed on own line, in order found.

