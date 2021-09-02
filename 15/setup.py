"""
118. Python Web Scraping - Grabbing a Title
"""
from requests import get
from bs4 import BeautifulSoup

if __name__ == "__main__":
    result = get("http://www.example.com")
    soup = BeautifulSoup(result.text, "lxml")
    print(soup.select("title")[0].get_text())
    site_paragraphs = soup.select("p")
    print(site_paragraphs[0].get_text(), "\n")
    res = get("https://en.wikipedia.org/wiki/Genshin_Impact")
    soup = BeautifulSoup(res.text, "lxml")
    for item in soup.select(".toctext"):
        print(item.text)
    image = soup.select(".thumbimage")[0]
    print(image["src"])
    image_link = get(f"https:{image['src']}")
    with open("../tmp/image.png", "wb") as file:
        file.write(image_link.content)
