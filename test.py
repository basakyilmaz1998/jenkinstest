import time
import requests

url = "https://example.com"

r1 = requests.get(url)
time.sleep(2)
r2 = requests.get(url)

assert r1.url == r2.url, "2. request farklı bir URL'e gitti!"
print("Test geçti: 2 saniye sonra aynı URL'e gidildi.")
