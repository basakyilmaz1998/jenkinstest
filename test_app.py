import time
import requests

def test_url_access():
    url = "https://example.com"

    r1 = requests.get(url)
    time.sleep(2)
    r2 = requests.get(url)

    assert r1.status_code == 200
    assert r2.status_code == 200
