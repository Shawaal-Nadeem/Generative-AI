# create a login function that takes in a username and password
import requests
def login(username, password):
    # check if the username and password are correct
    if username == "admin" and password == "admin":
        print("Login successful!")
    else:
        print("Invalid username or password.")

# create get function to fetch data with the help of api
def get(url):
    response = requests.get(url)
    return response.json()

    