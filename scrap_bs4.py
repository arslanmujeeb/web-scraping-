import requests
from bs4 import BeautifulSoup


url="https://scholar.google.com.pk/citations?user=kU2rwMAAAAAJ&hl=en&oi=ao"

r = requests.get(url)

soup = BeautifulSoup(r.content)
links=soup.find_all("a")

for link in links:
	if "http" in link.get("href"):
		print "<a href='%s'>%s </a>" %(link.get("href"), link.text)