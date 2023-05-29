import traceback
from typing import Dict, Union, List

import requests
from binance.spot import Spot
from binance.error import ClientError

from src.pydantic.models import OrderSides


class Trader:
    def __init__(self, api_key: str, api_secret: str, base_url: str) -> None:
        self.___precision: int = 6
        self.__symbol: str = 'BTCUSDT'
        self.__client: Spot = Spot(api_key=api_key, api_secret=api_secret, base_url=base_url)

    @property
    def precision(self) -> int:
        return self.___precision

    @precision.setter
    def precision(self, precision: int) -> None:
        try:
            self.___precision = int(precision)
        except Exception as e:
            print(e)

    @property
    def symbol(self) -> str:
        return self.__symbol

    @symbol.setter
    def symbol(self, symbol) -> None:
        try:
            self.__symbol = str(symbol)
        except Exception as e:
            print(e)

    def create_order(self, side: OrderSides, volume: float, price: float) -> Dict:
        params = {
            'symbol': self.__symbol,
            'side': side.value,
            'type': 'LIMIT',
            'timeInForce': 'GTC',
            'quantity': round(volume / price, self.___precision),
            'price': price
        }

        response: Dict = {
            'status_code': 200,
            'status': 'OK',
            'meta': params,
            'payload': {}
        }

        try:
            response['payload']: Dict = self.__client.new_order(**params)
        except ClientError as e:
            response['status_code'] = e.status_code
            response['status'] = e.error_message
            response['payload'] = f'Error code: {e.error_code}'
        except Exception as e:
            response['status_code'] = 400
            response['status'] = 'Error'
            response['payload'] = f'{type(e).__name__} occurred, args={str(e.args)}\n{traceback.format_exc()}'

        return response

    @property
    def account(self):
        try:
            return self.__client.account()
        except ClientError as e:
            return e
        except requests.exceptions.ConnectionError as e:
            return e
        except Exception as e:
            return e
