import pika

class RabbitmqConsumer:
    def  __init__(self, callback) -> None:
        self.__host = "localhost"
        self.__port = 5672
        self.__username = "guest"
        self.__password = "guest"
        self.__queue = "data_queue"
        self.__callback = callback
        self.__channel = self.create_channel()

    def create_channel(self):
    connection_parameters = pika.ConnectionParameters (
    host="localhost",
    port=5672,
    credentials=pika.PlainCredentials(
        self.__username = "guest",
        self.__password = "guest"
    )
)

channel = pika.BlockingConnection(connection_parameters).channel()
channel.queue_declare(
    queue="data_queue",
    durable=True
)

channel.basic_consume (
    queue="data_queue",
    auto_ack=True,
    on_message_callback= minha_callback
)

return channel