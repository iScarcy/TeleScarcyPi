
from tele import TeleP
from datetime import date
from datetime import datetime
import logging
import requests
import json
import configparser
import sys
import argparse

def reminder(event_type, event_date, log):
    print(event_date)
    url = "http://scarcypi:3002/api/eventi/"+ event_type + "/" + event_date
    print(url)
    print(event_type)
    data = requests.get(url).json()

    if not data:
        msg = "Nessun evento per oggi " + event_date
        TeleP(msg)
        return

    event_date_obj = date.fromisoformat(event_date)

    # Iterate through the JSON array
    for item in data:
        msg = ""
        item_date_obj = date.fromisoformat(item["data"])
                
        match(event_type):
            case "today":
                msg =  "Evento di oggi: " + item["type"] + " di " + item["description"] 
            case "data":
                msg =  "Evento del " + item["data"][5:10] + ": " + item["type"] + " di " +  item["description"] 
            case "month":
                msg =  "Evento del " + item["data"][5:10] + ": " + item["type"] + " di " +  item["description"] 
            case _:
                msg = "Evento del " + item["data"][5:10] + ": " + item["type"] + " di " +  item["description"] 
        TeleP(msg)
        logger.info(msg)

    logger.info("*** Events reminder, END ***")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Reminder eventi")
    parser.add_argument("-type", "--type", dest="event_type", default="today",
                        help="Tipo di ricerca (es: today)")
    parser.add_argument("-data", "--data", dest="event_date", default=str(date.today()),
                        help="Data in formato YYYY-MM-DD (es: 2025-11-20)")
    args = parser.parse_args()
    oggi = datetime.now().strftime("%Y-%m-%d")
    if args.event_type == "data":
        oggi = args.event_date
    logging.basicConfig(filename="log/events_reminder_" + oggi +  ".log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.info("*** Events reminder, START ***")
    
    reminder(event_type=args.event_type, event_date=args.event_date, log= logger)