"""
123. Python Web Scraping - Exercise Overview
"""
from requests import get
from bs4 import BeautifulSoup

if __name__ == "__main__":
    URL = "http://quotes.toscrape.com/page/"
    details = []
    PAGE = 1

    while True:
        PAGE_URL = URL + str(PAGE)
        res = get(PAGE_URL)
        if "No quotes found!" in res.text:
            break
        soup = BeautifulSoup(res.text, "lxml")
        for quote in soup.select(".quote"):
            details.append(
                {
                    "author": quote.select(".author")[0].text,
                    "text": quote.select(".text")[0].text,
                    "tags": [text.text for text in quote.select(".tags .tag")],
                }
            )
            print(details[-1], "\n")
        PAGE += 1
