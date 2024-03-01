import unittest
from unittest import mock
from tradingview_webhook_bot.emitter import EventEmitter


class EventEmitterTest(unittest.TestCase):
    @mock.patch('pika.BlockingConnection')
    def test_publish(self, mock_connection_constructor):
        mock_channel = mock.MagicMock()
        mock_connection = mock.MagicMock()
        mock_connection.channel.return_value = mock_channel
        mock_connection_constructor.return_value = mock_connection

        emitter = EventEmitter('amqp://guest:guest@localhost:5672/%2F')

        # Manually set the channel to mock channel
        emitter.channel = mock_channel

        test_message = "test message"
        test_exchange = "test exchange"

        emitter.publish(test_message, test_exchange)

        # Assert that basic_publish was called with correct parameters
        mock_channel.basic_publish.assert_called_once_with(exchange=test_exchange, routing_key='', body=test_message)


if __name__ == "__main__":
    unittest.main()
