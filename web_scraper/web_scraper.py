import requests
from bs4 import BeautifulSoup


# site to scrape
#   url = 'https://en.wikipedia.org/wiki/Nintendo'

# use 'requests' to grab information. Check for a response in terminal with a print statement
#   page = requests.get(url)

# use beautifulsoup to parse data
#   soup = BeautifulSoup(page.content, 'html.parser')

# grabbing a class, use class_ because it's a reserved word
#   results = soup.find(class_="course-details")

 # grab all headers in that class
 #  titles = results.find_all('h3')

# prints the text of titles
#   for title in titles:
#    print(title.text)

# makes another list in 'a' tag
#   anchors = results('a')
#   print(anchors)

# creates another list of just the links
#   links = (anchor['href'] for anchor in anchors)

# grabbing a single link from the list created above
#   401_link = links[1]

# manually build url link, build a new request page
#   new_url = 'https://en.wikipedia.org/' + 401_link

#   link_content = requests.get(new_url)

# use beautifulsoup to parse data again
#   link_soup = BeautifulSoup(link_content.content, 'html.parser')

# grabbing article in new data
#   article = link_soup('article')[1]

# select elements in article
# list_items = article.select(' ul li ul li ')

# loop through list items and print text
#   for li in list items:
#     print(li.text)


# --------------------------------------------------
# Scrape a Wikipedia page and record which passages need citations.


url = 'https://en.wikipedia.org/wiki/Nintendo'

def get_citations(url):
  page = requests.get(url)
  soup = BeautifulSoup(page.content, 'html.parser')
  
  citations_collected = []
  for paragraph in soup.find_all('p'):
    if paragraph.find(title="Wikipedia:Citation needed"):
      citations_collected.append(paragraph.get_text())
  return citations_collected

# print(get_citations(url))


# Your web scraper should report the number of citations needed.
# Count function must be named get_citations_needed_count
# get_citations_needed takes in a url and returns an integer

def get_citations_needed_count(url):
  count = get_citations(url)
  return len(count)

# print(get_citations_needed_count(url))


# Your web scraper should identify those cases AND include the relevant passage.
# E.g. Citation needed for “lorem spam and impsum eggs”
# Consider the “relevant passage” to be the parent element that contains the passage, often a paragraph element.

# Report function must be named get_citations_needed_report
# get_citations_needed_report takes in a url and returns a string
# the string should be formatted with each citation needed on own line, in order found.

def get_citations_needed_report(url):
  passages = ''
  citations = get_citations(url)

  for citation in citations:
    citation_list = citation.split()
    passages += ' '.join(citation_list) + '\n\n'
  return passages

print(get_citations_needed_report(url))



# Citation needed locations
#   - Branches - Nintendo of America x1
#   - Policy - Content Guidelines x1
#   - Policy - License Guidelines x1
#   - Policy - Intellectual property protection x1
