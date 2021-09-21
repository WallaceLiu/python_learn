#!/usr/bin/env python
"""

    To save logs to a file: python receive_logs.py > logs_from_rabbit.log
    To see logs on screen : python receive_logs.py


    exclusive=True, 只能启动一个 receive_logs.py, 再启动, 会抛如下异常

    pika.exceptions.ChannelClosedByBroker: (405, "RESOURCE_LOCKED - cannot obtain exclusive access to locked queue
    'log' in vhost '/'. It could be originally declared on another connection or
    the exclusive property value does not match that of the original declaration.")


    fanout exchange

    发送到该交换机的消息都会路由到与该交换机绑定的所有队列上，可以用来做广播
    不处理路由键，只需要简单的将队列绑定到交换机上
    Fanout交换机转发消息是最快的

"""
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

result = channel.queue_declare(exclusive=True, queue='log')
queue_name = result.method.queue  # 回调队列

channel.queue_bind(exchange='logs', queue=queue_name)

print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] %r" % body)


channel.basic_consume(on_message_callback=callback,
                      queue=queue_name,
                      auto_ack=False)

channel.start_consuming()
