import requests

response = requests.get('http://127.0.0.1:8000/hi/Shawaal Nadeem')

def test_get_request():
    assert response.status_code == 200

