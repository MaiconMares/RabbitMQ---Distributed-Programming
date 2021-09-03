import pika, sys, os, time

def main():

    def handle_message(ch, method, properties, body):
        print("Received {}".format(body.decode()))
        time.sleep(body.count(b'.'))
        ch.basic_ack(delivery_tag = method.delivery_tag)


    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='task_queue', durable=True)

    # Não permite receber mensagens se o worker estiver ocupado
    # processando alguma mensagem
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='task_queue',
                            on_message_callback=handle_message)

    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)