import requests 
from bs4 import BeautifulSoup

#for weather
def temperature():
    place = input("Enter the Place: ")
    search = f"Weather in {place}"
    url = f"https://www.google.com/search?&q={search}"
    r = requests.get(url)
    soup = BeautifulSoup(r.text,"html.parser")
    update = soup.find("div",class_="BNeawe").text
    print(f"{search} now is {update}")


