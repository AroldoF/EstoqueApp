from faststream import FastStream
from faststream.rabbit import RabbitBroker


broker = RabbitBroker("amqp://guest:guest@localhost/")
app = FastStream(broker)

