#!/usr/bin/env python

import pika

# Creating Connection
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
# Opening Channel
channel = connection.channel()

# Queue Declaration/Creation not necessary if decalred in send_message.py
channel.queue_declare(queue='queue1')


def callback(ch, method, properties, body):
    print("%r Message Recieved." % body)

channel.basic_consume(callback,
                      queue='queue1',
                      no_ack=True)

print("Waiting for Message. To Exit Press CTRL+C")
channel.start_consuming()
