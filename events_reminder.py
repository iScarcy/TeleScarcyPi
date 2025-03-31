from tele import TeleP
from datetime import date
import requests
    
import json 
import configparser
import sys

def reminder(today):
    print(today)
    url = "http://scarcypi:3002/api/eventi/today/" + today
    print(url)
    data = requests.get(url).json() 
    

    # Iterate through the JSON array
    for item in data:
        msg = ""
        match(item["type"]):
            case "Compleanno":
                anni = date(today).year - date(item["data"]).year  
                msg = "Oggi " + item["description"] + " compie " + str(anni) + " anni" 
                print(msg)
                return
            case "Onomastico":
                msg = "Oggi è l'onomastico di " + item["description"]  
                print(msg)
            case _:
                msg = "Evento di oggi " + str(item["data"]) + ": " + item["type"] + " di " + item["description"]    
                print(msg)
                return
        t = TeleP(msg)

if __name__ == "__main__":
    oggi = "2025-03-19"#str(date.today())
    reminder(today= oggi)