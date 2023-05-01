import cloudscraper
from bs4 import BeautifulSoup

artist_names = []
art_infos = []

base_url = "https://new.mta.info/agency/arts-design/permanent-art/nyct-queens"

scraper = cloudscraper.create_scraper()

#loop through 
page = scraper.get(base_url) 

print (page.text)
soup= BeautifulSoup(page.text)

artworks = soup.find_all('a', {"class":"mta-card mta-flex mta-flex-grow mta-flex-col"})

for artwork in artworks:
	artist = artwork.find('span', {'class':"mta-card-title mta-font-bold"})
	artinfo = artwork.find('span', {'class':"mta-card-title mta-block mta-text-2xl mta-leading-600 mta-mt-100"})
	print(artist.text.strip()) , print(artinfo.text.strip())


