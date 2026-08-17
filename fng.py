import requests

URL = "https://production.dataviz.cnn.io/index/fearandgreed/graphdata"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Referer": "https://edition.cnn.com/markets/fear-and-greed",
    "Accept": "application/json, text/plain, */*",
}

response = requests.get(URL, headers=HEADERS, timeout=10)
response.raise_for_status()

score = response.json()["fear_and_greed"]["score"]
data = str(round(score))

with open("fng.txt", "w", encoding="utf-8") as f:
    f.write(data)

print(data)
