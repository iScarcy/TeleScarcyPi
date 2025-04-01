from tele import TeleP
from datetime import date
from datetime import datetime
import requests
    

def reminder(today):
    
    url = "http://scarcypi:3002/api/eventi/today/" + today
    print(url)
    data = requests.get(url).json() 
    
    todayDate = datetime.strptime(today, '%Y-%m-%d').date()
    # Iterate through the JSON array
    for item in data:
        msg = ""
        dateEvent = datetime.strptime(item["data"], '%Y-%m-%d').date()
        print(item["type"])
        match(item["type"]):
            case "Compleanno":
                anni = todayDate.year - dateEvent.year  
                msg = "Oggi " + item["description"] + " compie " + str(anni) + " anni" 
                print(msg)
                
            case "Onomastico":
                msg = "Oggi è l'onomastico di " + item["description"]  
                print(msg)
               
            case _:
                msg = "Evento di oggi " + str(item["data"]) + ": " + item["type"] + " di " + item["description"]    
                print(msg)
              
        t = TeleP(msg)

if __name__ == "__main__":
    oggi = str(date.today())
    reminder(today= oggi)