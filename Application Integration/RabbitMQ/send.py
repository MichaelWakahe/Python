#!/usr/bin/env python
import pika

'''
Sends a message to a RabbitMQ queue

Adapted from: https://www.rabbitmq.com/tutorials/tutorial-one-python.html
'''

# Set the connection parameters to connect to localhost on port 5672
# on the / virtual host using the username "grobbitmq" and password "dummy_password"
credentials = pika.PlainCredentials('username', 'password')
parameters = pika.ConnectionParameters('localhost',
                                       5672,
                                       '/',
                                       credentials)

connection = pika.BlockingConnection(parameters)

# Connect to a broker on the local machine
channel = connection.channel()


# Let's create a hello queue to which the message will be delivered:
channel.queue_declare(queue='hello')


# In RabbitMQ a message can never be sent directly to the queue, it always needs to go through an exchange.
# A default exchange identified by an empty string. This exchange is special - it allows us to specify exactly to which
# queue the message should go. The queue name needs to be specified in the routing_key parameter.
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello Michael!')
print(" [x] Sent 'Hello Michael!'")


# Before exiting the program we need to make sure the network buffers were flushed and our message was actually
# delivered to RabbitMQ. We can do it by gently closing the connection.
connection.close()
