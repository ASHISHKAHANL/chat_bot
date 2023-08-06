import random
from chatting import opeaning 
from chatting import time_1
from chatting import day
from chatting import news
from chatting import temperature 


print(random.choice(opeaning.greeting))
user = input("Ashish:")

if user=="time":
    time_1.times()
    
elif user == "day": 
    day.days()

elif user == "news":
    news.news()
    
elif user == "temperature":
    temperature.temp()  




