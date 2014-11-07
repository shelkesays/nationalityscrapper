import requests
import bs4
import csv
import re


page = requests.get("http://geography.about.com/library/weekly/aa030900a.htm")
'''
page = requests.get("
https://www.englishclub.com/vocabulary/world-countries-nationality.htm")
'''
soup = bs4.BeautifulSoup(page.text)
# write to csv
csvfile = open("test.csv", "wb")
wr = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

# This will fetch table
table = soup.find_all("tr")
countrylist = []
for row in table:
    nationality = []
    for column in row:
        if isinstance(column, basestring):
            column = column.strip()
        if column:
            nationality.append(
                re.sub(r'\(.*?\)', '',
                       ''.join(column.find_all(text=True))).strip())
    wr.writerow(nationality)
