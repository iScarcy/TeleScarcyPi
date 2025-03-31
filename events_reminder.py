from tele import TeleP
from datetime import date
import requests
    
import json 
import configparser
import sys

def reminder(today):
    print(today)
    url = "http://scarcypi:3002/api/eventi?oggi=" + today
    print(url)
    data = requests.get(url).json() 
    

    # Iterate through the JSON array
    for item in data:
        msg = "Oggi è il " + item["type"] + " di " + item["description"]
        print(msg)
  #  t = TeleP(msg)

if __name__ == "__main__":
    oggi = str(date.today())
    reminder(today= oggi)