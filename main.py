import configparser
from rabbitmq import RabbitMQ
import sys

def callback(ch, method, properties, body):
    print(f"Received message: {body}")

def main():
    config = configparser.ConfigParser()
    config.sections()
    config.read('config.ini')
    config.sections()
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