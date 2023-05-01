import cloudscraper
from bs4 import BeautifulSoup
import csv

artist_names = []
art_infos = []

base_url = "https://new.mta.info/agency/arts-design/permanent-art/manhattan"

scraper = cloudscraper.create_scraper()

#loop through 
page = scraper.get(base_url) 

soup = BeautifulSoup(page.text)

artworks = soup.find_all('a', {"class":"mta-card mta-flex mta-flex-grow mta-flex-col"})

res = []

for artwork in artworks:
    artist_html = artwork.find('span', {'class':"mta-card-title mta-font-bold"})
    artinfo_html = artwork.find('span', {'class':"mta-card-title mta-block mta-text-2xl mta-leading-600 mta-mt-100"})
    artinfo = { 'artist': artist_html.text.strip()}
    artinfo_parts = artinfo_html.text.strip().split('•')
    artinfo['title'] = artinfo_parts[0]
    artinfo['date'] = artinfo_parts[1]
    artinfo['location'] = artinfo_parts[2]
    res.append(artinfo)

with open('manhattan.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['artist', 'title', 'date', 'location'])
    for artwork in res:
        writer.writerow([artwork['artist'], artwork['title'], artwork['date'], artwork['location']])




