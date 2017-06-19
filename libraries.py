# import libraries
import sys
from bs4 import BeautifulSoup
# Determine which urllib library to use
if sys.version_info[0] < 3:
    from urllib2 import urlopen
else:
    from urllib.request import urlopen

# Use the exact URL you want to scrape
locations = 'http://library.austintexas.gov/locations'

# Use urllib2 or urllib to pull the html to the variable 'site'
site = urlopen(locations)

# Parse the site
soup = BeautifulSoup(site, 'html.parser')

# Retrieve data
all_locations = soup.find_all('div', attrs = {"apl-box"})

for loc in all_locations:
    print(loc.find('h2', attrs = 'pane-title').text)
