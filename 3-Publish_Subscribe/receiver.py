import pika, sys, os

def main():

    def handle_message(ch, method, properties, body):
        print('(consumer) Received message: {}'.format(body))

    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Cria um exchange que envia todas as mensagens que chega a ele a
    # todas as filas que ele conhece
    channel.exchange_declare(exchange='logs', exchange_type='fanout')

    # Cria uma nova fila com nome aleatorio toda vez que o server
    # reinicia
    result = channel.queue_declare(queue='', exclusive=True)

    # Relaciona um exchange a uma fila
    channel.queue_bind(exchange='logs', queue=result.method.queue)

    channel.basic_consume(queue=result.method.queue,
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