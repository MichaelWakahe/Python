#!/usr/bin/env python
import pika

'''
Gets a message to a RabbitMQ queue

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


# We create a hello queue just in case this application runs before the Producer
channel.queue_declare(queue='hello')


# Receiving messages from the queue is more complex. It works by subscribing a callback function to a queue. Whenever we
# receive a message, this callback function is called by the Pika library. In our case this function will print on the
# screen the contents of the message.
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


# Next, we need to tell RabbitMQ that this particular callback function should receive messages from our hello queue:
channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)


# And finally, we enter a never-ending loop that waits for data and runs callbacks whenever necessary.
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
