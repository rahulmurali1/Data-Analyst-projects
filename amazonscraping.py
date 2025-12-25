import requests
from bs4 import BeautifulSoup

def main(URL):
    File = open("output.csv", "a")

    Headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9"
    }
    try:
        webpage = requests.get(URL, headers=Headers)
        soup = BeautifulSoup(webpage.content, "lxml")
    except requests.exceptions.MissingSchema:
        print("Invalid URL")

    try:
        title = soup.find("span", attrs={'id':'productTitle'}).string.strip().replace(",", "")
    except AttributeError:
        title = "Na"
    print("Product title= ", title)
    File.write(f"{title},")

    try:
        price= soup.find("span", class_ = "a-price-whole").string.strip().replace(",", "")
    except AttributeError:
        price = "na"
    print("Price= ", price)
    File.write(f"{price},")

    try:
        rating = soup.find("span", class_ = "a-size-small a-color-base").string.strip().replace(",", "")
    except AttributeError:
        rating = "NA"
    print("Product rating= ", rating)
    File.write(f"{rating},")

    try:
        review_count = soup.find("span", attrs={"id": "acrCustomerReviewText"}).string.strip().replace(",", "")
    except AttributeError:
        review_count = "Na"
    print("Review count= ", review_count)
    File.write(f"{review_count},\n")

    File.close()

if __name__ == '__main__':
    file = open("links.txt", "r")
    for links in file.readlines():
        try:
            main(links)
        except UnboundLocalError:
            print("cannot access link")

