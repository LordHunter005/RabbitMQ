#!/usr/bin/env python

import pika

# Creating Connection
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
# Opening Channel
channel = connection.channel()

# Exchange Declaration/Creation not necessary if decalred in emit_log.py
channel.exchange_declare(exchange='logs',
                         exchange_type='fanout')

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='logs',
                   queue=queue_name)


def callback(ch, method, properties, body):
    print("Message Recieved %r" % body)

channel.basic_consume(callback,
                      queue=queue_name)

print("Waiting for Message. To Exit Press CTRL+C")
channel.start_consuming()

# Run this file as $python recieve_logs.py > logs_from_rabbit.log
# Run emit_log.py
