from tele import TeleP
from datetime import date
from datetime import datetime
import logging
import requests
    

def reminder(today, log):
    
    url = "http://scarcypi:3002/api/eventi/today/" + today
    logger.info("Events reminder, url:" + url )
    data = requests.get(url).json() 
    logger.info(str(len(data)) + " events was found")
    todayDate = datetime.strptime(today, '%Y-%m-%d').date()
    # Iterate through the JSON array
    for item in data:
        msg = ""
        dateEvent = datetime.strptime(item["data"], '%Y-%m-%d').date()
        
        match(item["type"]):
            case "Compleanno":
                anni = todayDate.year - dateEvent.year  
                msg = "Oggi " + item["description"] + " compie " + str(anni) + " anni" 
                
                
            case "Onomastico":
                msg = "Oggi è l'onomastico di " + item["description"]  
                
               
            case _:
                msg = "Evento di oggi " + str(item["data"]) + ": " + item["type"] + " di " + item["description"]    
                
        logger.info("msg:" + msg)      
        t = TeleP(msg)

    logger.info("*** Events reminder, END ***")

if __name__ == "__main__":
    oggi = str(date.today())
    logging.basicConfig(filename="log/events_reminder_" + oggi +  ".log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.info("*** Events reminder, START ***")
    logger.info("today:" + oggi)
    reminder(today= oggi, log= logger)