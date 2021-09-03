import pika

# Inicia a conexão e cria o canal de conexao
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Cria a fila se ela não existir
channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',
                        routing_key='hello',
                        body='Bonjour, comment-allez vous?')

print('(producer): Message sent!')

connection.close()
