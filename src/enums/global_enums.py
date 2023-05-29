from enum import Enum


class GlobalErrorMessages(Enum):
    ORDERS_COUNT_ERROR = 'Order volumes quantity is not equal to expected.'
    ORDERS_SUM_ERROR = 'Order volumes sum is not equal to expected.'
    ORDERS_VOLUME_ERROR = 'Order volume is out of expected range.'
    BINANCE_CONNECTION_ERROR = 'Unable to connect to Binance'
    BINANCE_API_KEY_ERROR = 'Unable to connect to Binance'
    BINANCE_SECRET_KEY_ERROR = 'Unable to connect to Binance'
