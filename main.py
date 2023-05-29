import json
import random
from typing import Dict, List
from fastapi import FastAPI

from utils import gen_random_volumes
from config import API_KEY, SECRET_KEY, BASE_URL
from src.classes.trader import Trader
from src.pydantic.models import OrderDataModel, OrderStatusModel

app: FastAPI = FastAPI(title="Test assignment")


@app.post('/api/v1/orders')
def create_orders(data: OrderDataModel) -> List[OrderStatusModel]:
    volumes: List = gen_random_volumes(volume=data.volume,
                                       quantity=data.number,
                                       amountDif=data.amountDif)
    response: List = []
    trader: Trader = Trader(api_key=API_KEY, api_secret=SECRET_KEY, base_url=BASE_URL)
    for volume in volumes:
        price: float = round(random.uniform(data.priceMin, data.priceMax), 2)
        response.append(trader.create_order(side=data.side, volume=volume, price=price))
    return response
