# import datetime 
# import time
# import requests 
# from bs4 import BeautifulSoup

# now = datetime.datetime.now()
# print("current date and time:")
# print(now.strftime("Date: %d/%m/%Y\n\nTime: %H:%M:%S"))

# date_now = datetime.date.today()
# print(date_now)

#print(time.strftime("%H:%M:%S")) #24 hour format

#print(time.strftime("%I:%M:%S %p"))  #12 hour format

# print(time.strftime("%A"))   #for sunday,monday etc..


#for weather

# place = input("Enter the Place: ")
# search = f"Weather in {place}"
# url = f"https://www.google.com/search?&q={search}"
# r = requests.get(url)
# soup = BeautifulSoup(r.text,"html.parser")
# update = soup.find("div",class_="BNeawe").text
# print(f"{search} now is {update}")




#for news

# api_key = "3ea7ba33a91a4849a3d2be50ec996961"
# def news():
#     main_url = "https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=" + api_key
#     news= requests.get(main_url).json()
#    # print(news)
#     article = news["articles"]

#     news_article = []
#     for arti in article:
#         news_article.append(arti['title'])

#     for i in range(5):
#         print(i+1,news_article[i])


# news()