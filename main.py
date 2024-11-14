from rabbitmq import RabbitMQ
from tele import TeleP
import json 
import configparser
import sys
 
# Channel ID Sample: -1001829542722

 

def callback(ch, method, properties, body):
    print(" [x] Received %r" % json.loads(body))
    data = json.loads(body)
    msg = data["msg"]
    print(msg)
    t = TeleP(msg)
    
def main():
    config = configparser.ConfigParser()
    config.sections()
    config.read('config.ini')
    host     = config['RABBIT']['host']
    user     = config['RABBIT']['user']
    port = config['RABBIT']['port']
    password = config['RABBIT']['passwd']
    queue_event = config['RABBIT']['queue_event']

    rabbitmq = RabbitMQ(host=host, user=user, password=password, port=port)
    try:
        print("Connection to RabbitMQ established successfully.")
        rabbitmq.consume(queue_name=queue_event, callback=callback)
    except Exception as e:
        print(f"Failed to establish connection to RabbitMQ: {e}")
        sys.exit(1)
    finally:
        rabbitmq.close()

if __name__ == "__main__":
    main()