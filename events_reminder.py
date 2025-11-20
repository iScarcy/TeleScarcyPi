# ...existing code...
from tele import TeleP
from datetime import date
from datetime import datetime
import logging
import requests
import json
import configparser
import sys
import argparse

def reminder(event_type, event_date):
    print(event_date)
    url = "http://scarcypi:3002/api/eventi/"+ event_type + "/" + event_date
    print(url)
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
        match(item["type"]):
            case "Compleanno":
                # Calcolo età considerando mese/giorno
                anni = event_date_obj.year - item_date_obj.year - (
                    (event_date_obj.month, event_date_obj.day) < (item_date_obj.month, item_date_obj.day)
                )
                msg = "Oggi " + item["description"] + " compie " + str(anni) + " anni"
                print(msg)
                TeleP(msg)
                # non return per gestire eventuali altri eventi nella lista
            case "Onomastico":
                msg = "Oggi è l'onomastico di " + item["description"]
                print(msg)
                TeleP(msg)
            case _:
                msg = "Evento di oggi " + str(item["data"]) + ": " + item["type"] + " di " + item["description"]
                print(msg)
                TeleP(msg)
# ...existing code...

    logger.info("*** Events reminder, END ***")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Reminder eventi")
    parser.add_argument("-type", "--type", dest="event_type", default="today",
                        help="Tipo di ricerca (es: today)")
    parser.add_argument("-data", "--data", dest="event_date", default=str(date.today()),
                        help="Data in formato YYYY-MM-DD (es: 2025-11-20)")
    args = parser.parse_args()

    reminder(event_type=args.event_type, event_date=args.event_date)