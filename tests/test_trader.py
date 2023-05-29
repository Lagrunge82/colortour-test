import pytest
import requests

from src.classes.trader import Trader
from config import API_KEY, SECRET_KEY, BASE_URL
from src.enums.global_enums import GlobalErrorMessages
from binance.error import ClientError

trader: Trader = Trader(api_key=API_KEY, api_secret=SECRET_KEY, base_url=BASE_URL)
account = trader.account


def test_connection():
    print(account)
    assert not isinstance(account, requests.exceptions.ConnectionError), \
        GlobalErrorMessages.BINANCE_CONNECTION_ERROR.value


def test_api_key():
    test_connection()
    assert (not isinstance(account, ClientError) or trader.account.error_code == -1022), \
        GlobalErrorMessages.BINANCE_API_KEY_ERROR.value


def test_secret_key():
    test_connection()
    assert (not isinstance(account,
                           ClientError) or trader.account.error_code == -2014), \
        GlobalErrorMessages.BINANCE_SECRET_KEY_ERROR.value
