from bs4 import BeautifulSoup
import requests

search = input("Enter Search Term:")
params = {"q": search}
r = requests.get("https://www.google.com/search", params = params)

soup = BeautifulSoup(r.text, "html.parser")
print(soup.prettify())