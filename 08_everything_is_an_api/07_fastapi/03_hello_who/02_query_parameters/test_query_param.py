import requests

params = {"who": "Shawaal"}
r = requests.get("http://127.0.0.1:8000/hi", params=params)
print(r.json())