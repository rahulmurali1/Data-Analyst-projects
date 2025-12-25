import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.imdb.com/chart/top/"
headers = {
    "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) ""AppleWebKit/537.36 (KHTML, like Gecko) ""Chrome/120.0.0.0 Safari/537.36",
    "Accept-language": "en-US,en;q=0.9"
}
response = requests.get(url, headers= headers)
soup = BeautifulSoup(response.text, "html.parser")
soup = BeautifulSoup(response.text, "html.parser")

movies = soup.select("li.ipc-metadata-list-summary-item")
movies_data = []

for movie in movies:
    title = movie.select_one("h3.ipc-title__text").text.strip()
    year = movie.select_one("span.cli-title-metadata-item").text.strip()
    rating_tag = movie.select_one("span.ipc-rating-star--rating")
    rating = rating_tag.text.strip() if rating_tag else "N/A"

    movies_data.append({
        "Title": title,
        "Year": year,
        "Rating": rating
    })

for movie in movies_data:
    print(f"{movie['Title']} ({movie['Year']}) - Rating: {movie['Rating']}")

df = pd.DataFrame(movies_data)
df.to_csv("imdb_top_250_movies.csv", index=False)
print("IMDb data saved successfully to imdb_top_250_movies.csv!")    
