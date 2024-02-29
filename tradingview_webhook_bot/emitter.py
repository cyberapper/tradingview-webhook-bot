import pika


class EventEmitter:
    def __init__(self, connection_url: str):
        self.connection_url = connection_url
        self.connection = None
        self.channel = None

    def _establish_connection(self):
        if not self.connection:
            # Create a new connection
            parameters = pika.URLParameters(self.connection_url)
            self.connection = pika.BlockingConnection(parameters)
            # Create channel on the connection
            self.channel = self.connection.channel()
            self.channel.queue_declare(queue='crescendo', durable=True)

    def _close_connection(self):
        if self.connection:
            self.connection.close()
            self.connection = None
            self.channel = None

    def publish(self, message: str, exchange: str = ""):
        self._establish_connection()

        # Publish the message
        self.channel.basic_publish(
            exchange=exchange,
            routing_key='crescendo',
            body=message,
            properties=pika.BasicProperties(
                delivery_mode=pika.DeliveryMode.Persistent
            )
        )
        print(f"Published message: '{message}' to exchange: '{exchange}'")
        self._close_connection()


if __name__ == "__main__":
    emitter = EventEmitter('amqp://guest:guest@localhost:5672/%2F')
    emitter.publish('test message', '')
