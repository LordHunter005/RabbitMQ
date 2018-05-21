#!/usr/bin/env python

import pika

# Creating Connection
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
# Opening Channel
channel = connection.channel()

# Queue Declaration/Creating
channel.queue_declare(queue='queue1')

# Publishing/Sending Message
channel.basic_publish(exchange='',
                      routing_key='queue1',
                      body='Hello World!')

print("Message Sent...")
# Closing Channel
channel.close()
