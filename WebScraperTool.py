import requests
from bs4 import BeautifulSoup
import csv

# Example Jordanian news website (Al Ghad)
URL = "https://alghad.com/"

def fetch_headlines(url):
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, "html.parser")
    headlines = [h.get_text(strip=True) for h in soup.select("h3 a")]
    return headlines

def save_to_csv(headlines, filename="headlines.csv"):
    with open(filename, mode="w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Headline"])
        for headline in headlines:
            writer.writerow([headline])

if __name__ == "__main__":
    headlines = fetch_headlines(URL)
    save_to_csv(headlines)
    print(f"Saved {len(headlines)} headlines to headlines.csv")