import requests
from bs4 import BeautifulSoup
import csv
from app import db
from app.models import Book, Author


def get_html(url):
    r = requests.get(url)
    print(f"Request to {url}. Status code {r.status_code}")
    return r.text


def get_date(html):
    soup = BeautifulSoup(html, 'lxml')
    titles = soup.find("div", class_="products-row-outer").find_all("div", class_="card-column")
    for title in titles:
        title_book = title.find('div', class_='product-cover').find("span", class_="product-title").text
        author = title.find('div', class_='product-author').find("a").get("title")
        count_book = Book.query.filter(Book.title == title_book).count()
        if count_book == 0:
            book = Book(title=title_book)
            db.session.add(book)
            db.session.commit()
    print("Книги добавлены")


def main():
    url = "https://www.labirint.ru/search/%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5/?stype=0&page=1"
    get_date(get_html(url))


if __name__ == "__main__":
    main()