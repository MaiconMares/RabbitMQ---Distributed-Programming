import pika

# Inicia a conexão e cria o canal de conexao
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Cria um exchange que envia todas as mensagens que chega a ele a
# todas as filas que ele conhece
channel.exchange_declare(exchange='logs', exchange_type='fanout')

channel.basic_publish(exchange='logs',
                        routing_key='',
                        body='Bonjour, comment-allez vous?')

print('(producer): Message sent!')

connection.close()
