import json
import re
import signal
import configparser
from rabbitmq import RabbitMQ
import sys
from pathlib import Path

class SignalHandler:
    shutdown_requested = False

    def __init__(self):
        signal.signal(signal.SIGINT, self.request_shutdown)
        signal.signal(signal.SIGTERM, self.request_shutdown)

    def request_shutdown(self, *args):
        print('Request to shutdown received, stopping')
        self.shutdown_requested = True

    def can_run(self):
        return not self.shutdown_requested

config = configparser.ConfigParser()
config.sections()
config.read('config.ini')
config.sections()
host     = config['RABBIT']['host']
user     = config['RABBIT']['user']
port = config['RABBIT']['port']
password = config['RABBIT']['passwd']
queue_event = config['RABBIT']['queue_event']

signal_handler = SignalHandler()
urls = [
    'https://books.toscrape.com/catalogue/sapiens-a-brief-history-of-humankind_996/index.html',
    'https://books.toscrape.com/catalogue/shakespeares-sonnets_989/index.html',
    'https://books.toscrape.com/catalogue/sharp-objects_997/index.html',
]

def callback(ch, method, properties, body):
    print(f"Received message: {body}")
    
index = 0
while signal_handler.can_run():
    rabbitmq = RabbitMQ(host=host, user=user, password=password, port=port)
    try:
        print("Connection to RabbitMQ established successfully.")
        rabbitmq.consume(queue_name=queue_event, callback=callback)
    except Exception as e:
        print(f"Failed to establish connection to RabbitMQ: {e}")
        sys.exit(1)
    finally:
        rabbitmq.close()



  #  print('Scraping url', url)
 