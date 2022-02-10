# Project Name

**Author**: Clarissa
**Version**: 1.0.2

## Overview
<!-- Provide a high level overview of what this application is and why you are building it, beyond the fact that it's an assignment for this class. (i.e. What's your problem domain?) -->
Building a web scraper to scrape a Wikipedia page that has multiple needed citations.

Scrape a Wikipedia page and record which passages need citations

Your web scraper should report the number of citations needed

Your web scraper should identify those cases AND include the relevant passage

User Acceptance Tests:

- verify that correct count of citations needed is calculated

- verify the preceding passage

## Getting Started
<!-- What are the steps that a user must take in order to build this app on their own machine and get it running? -->
create directory/file -> poetry init -> poetry shell -> open
import requests (in terminal and file) ->

Assign URL link to a variable  
use requests.get() to access site with requests library

Test for a successful response

poetry add bs4 (adds beautiful soup library to work with parsing)

parse the data with BeautifulSoup()

## Change Log
<!-- Use this area to document the iterative changes made to your application as each feature is successfully implemented. Use time stamps. Here's an example:

01-01-2001 4:59pm - Application now has a fully-functional express server, with a GET route for the location resource. -->

2-5-22 - created get_citations function to record which passages need citations

2-7-22 - created get_citations_needed_count to count citations needed  
created get_citations_needed_report function to report citations with their passages

## Credit and Collaborations
<!-- Give credit (and a link) to other people or resources that helped you build this application. -->

Brandon - TA
Kassie - TA

[Beautiful Soup Docs](https://beautiful-soup-4.readthedocs.io/en/latest/index.html?highlight=pretty#output)
