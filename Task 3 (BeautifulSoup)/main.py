import requests
from bs4 import BeautifulSoup


url = "https://www.indiatoday.in/"



response = requests.get(url)
response.raise_for_status()
soup = BeautifulSoup(response.text, "html.parser")

#To get H2 headlines

headlines = [] # creating empty list

for headline in soup.find_all("h2"):
    text = headline.get_text(strip = True)
    if text and text not in headlines:
        headlines.append(text)

#Here i will save fetched headlines in a file

with open("html-file/headlines.txt" , "w", encoding ="utf-8") as f:
    for h in headlines:
        f.write(h + "\n")

print(f"Scraped {len(headlines)} headlines. Saved to headlines.txt")

