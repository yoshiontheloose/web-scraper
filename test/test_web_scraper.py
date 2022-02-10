from web_scraper import web_scraper


# verify that correct count of citations needed is calculated
def test_citation_count():
  url = 'https://en.wikipedia.org/wiki/Nintendo'
  actual = web_scraper.get_citations_needed_count(url)
  expected = 4
  assert actual == expected

# verify that preceding passage
def test_passage_report():
  url = 'https://en.wikipedia.org/wiki/Nintendo'
  report = web_scraper.get_citations_needed_report(url)
  passage = "Nintendo of America's Canadian branch, Nintendo of Canada, is based in Vancouver, British Columbia with a distribution center in Toronto, Ontario."
  assert passage in report
  
def test_passage_second_report():
  url = 'https://en.wikipedia.org/wiki/Nintendo'
  report = web_scraper.get_citations_needed_report(url)
  passage = "However, the release of the Wii was accompanied by several even more controversial games, such as Manhunt 2, No More Heroes, The House of the Dead: Overkill, and MadWorld, the latter three of which were published exclusively for the console."
  assert passage in report

  