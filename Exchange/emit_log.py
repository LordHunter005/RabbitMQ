#!/usr/bin/env python

import pika
import time

# Creating Connection
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
# Opening Channel
channel = connection.channel()

# Exchange Declaration/Creation
channel.exchange_declare(exchange='logs',
                         exchange_type='fanout')

for i in range(20):
    # Publishing/Sending Message
    channel.basic_publish(exchange='logs',
                          routing_key='',
                          body='Hello World %r' % i)
    time.sleep(1)
    print("Message Sent %r ..." % i)
# Closing Channel
channel.close()
