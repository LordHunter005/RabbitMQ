#!/usr/bin/env python

import pika
import time

# Creating Connection
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
# Opening Channel
channel = connection.channel()

# Queue Declaration/Creating
channel.queue_declare(queue='queue1')

for i in range(20):
    # Publishing/Sending Message
    channel.basic_publish(exchange='',
                          routing_key='queue1',
                          body='Hello World %r' % i)
    time.sleep(1)
    print("Message Sent %r ..." % i)
# Closing Channel
channel.close()
