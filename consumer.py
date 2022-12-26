import pika
import json, threading
from notify.functions import to_one_user, to_all_users
from notify.database import UserToken


def callback(ch, method, properties, body):
    data = json.loads(body)
    senderId = data['senderId']
    userId = data['userId']
    msg = data['message']
    profile = UserToken.query.filter_by(userId=userId).first()

    if profile:
        to_one_user(profile=profile, message=msg, senderId=senderId, notificationType=None)


def receive_command():
    print("ENTERED")
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    
    channel.exchange_declare(exchange='notification_ex', exchange_type='direct')

    result = channel.queue_declare(queue='notification_qu', durable=True)
    queue_name = result.method.queue


    channel.queue_bind(exchange='notification_ex', queue=queue_name, routing_key='notification_key')


    print(' [*] Waiting for logs. To exit press CTRL+C')

    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

    channel.start_consuming()


def start():
    t_msg = threading.Thread(target=receive_command)
    t_msg.start()
    t_msg.join(0)
    #self.receive_command()