# import libraries
import sys
import csv
from bs4 import BeautifulSoup
# Determine which urllib library to use
if sys.version_info[0] < 3:
    from urllib2 import urlopen
else:
    from urllib.request import urlopen

def makesoup(url):
    site = urlopen(url)
    return BeautifulSoup(site, 'html.parser')

locations = 'http://library.austintexas.gov/locations'
soup = makesoup(locations)
all_locations = soup.find_all('div', attrs = {"apl-box"})
writer = csv.writer(open("locations.csv", 'w'))

for loc in all_locations:
    if loc.find('div', attrs = {'views-field-field-address'}):
        current = []
        current.append(loc.find('h2', attrs = 'pane-title').text)
        print(loc.find('h2', attrs = 'pane-title').text)
        current.append(loc.find('div', attrs = {'views-field-field-address'}).text)
        print(loc.find('div', attrs = {'views-field-field-address'}).text)
        writer.writerow(current)
