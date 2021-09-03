import pika, sys, os

def main():

    def handle_message(ch, method, properties, body):
        print('(consumer) Received message: {}'.format(body))

    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    channel.basic_consume(queue='hello',
                            auto_ack=True,
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