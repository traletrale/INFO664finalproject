import cloudscraper
from bs4 import BeautifulSoup

artist_names = []
art_infos = []

base_url = "https://www.nyc.gov/assets/dclapercentforart/js/pages/panyc.js"

scraper = cloudscraper.create_scraper()

print ()

# loop through all project pages
#for page in range(0):
#    params = {"recordID": page}
#    htmldoc = scraper.get(base_url, params=params)
#    soup = BeautifulSoup(htmldoc.text, "html.parser")

    # print soup to inspect HTML content
#    print(soup)

    # scrape artist names
#   artists_container = soup.find("section", {"data-grid": "artists"})
#    artists = artists_container.find_all("li")
#    for artist in artists:
#        artist_names.append(artist.find("h3").text.strip())

    # scrape artwork information
#    title = soup.find("h2", {"class": "entry-title"}).text.strip()
#   date = soup.find("div", {"class": "proj-date"}).text.strip()
#   art_info = {
#        "date": date,
#        "title": title
#    }
#    art_infos.append(art_info)

# print results
#print(artist_names)
#print(len(artist_names))
#print(art_infos)

# print results
#print(artist_names)
#print(len(artist_names))
#print(art_infos)


#import cloudscraper
#import requests
#from bs4 import BeautifulSoup

#artist_names = []
#art_info = []

#base_url = "https://www.nyc.gov/site/dclapercentforart/projects/projects-detail.page?recordID=271"
#page = 0
#while page <=271:
#     while page <= 0:

#      params = {"recordID": page}
#      page = page + 1
#      scraper = cloudscraper.create_scraper()
#      htmldoc = scraper.get(base_url, params=params)


#soup = BeautifulSoup(htmldoc.text)
#art_info = {
#	 "date": date,
#	 "title": title
#	 }
#art_infos.append(art_info)
#artists_container = soup.find("section", {"data-grid":"artists"})
#artists = artists_container.find_all("li")
#for artist in artists:
# artist_names.append(artist.find('h3').text.strip())

#print(artist_names)
#print(len(artist_names))

#every noise at once
#use lowercase for the met api