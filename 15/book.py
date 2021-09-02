"""
121. Python Web Scraping - Book Examples Part One
"""
from requests import get
from bs4 import BeautifulSoup

if __name__ == "__main__":
    BASE_URL = "http://books.toscrape.com/catalogue/page-{}.html"
    two_star_titles = []
    for num in range(1, 51):
        SCRAPE_URL = BASE_URL.format(num)
        res = get(SCRAPE_URL)
        soup = BeautifulSoup(res.text, "lxml")
        books = soup.select(".product_pod")
        for book in books:
            if len(book.select(".star-rating.Two")) != 0:
                book_title = book.select("a")[1]["title"]
                print(book_title)
                two_star_titles.append(book_title)
