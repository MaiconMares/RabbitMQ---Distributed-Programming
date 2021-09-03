import pika, sys

# Inicia a conexão e cria o canal de conexao
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Cria a fila se ela não existir
channel.queue_declare(queue='task_queue', durable=True)

message = ' '.join(sys.argv[1:]) or 'Hello World...'

channel.basic_publish(exchange='',
                        routing_key='task_queue',
                        body=message,
                        properties=pika.BasicProperties(
                        delivery_mode=2 # Torna a mensagem persistente
))

print('(producer): Message sent!')

connection.close()
