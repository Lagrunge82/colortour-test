from enum import Enum
from typing import List, Union, Dict
from pydantic import BaseModel, Field


class OrderSides(Enum):
    sell = 'SELL'
    buy = 'BUY'


class OrderDataModel(BaseModel):
    volume: float = Field(gt=0)
    number: int = Field(gt=0)
    amountDif: float = Field(ge=0)
    side: OrderSides
    priceMin: float = Field(gt=0)
    priceMax: float = Field(gt=0)


class OrderMetaModel(BaseModel):
    symbol: str
    side: OrderSides
    type: str
    timeInForce: str
    quantity: float
    price: float


class OrderPayloadModel(BaseModel):
    symbol: str
    orderId: int
    orderListId: int
    clientOrderId: str
    transactTime: int
    price: str
    origQty: str
    executedQty: str
    cummulativeQuoteQty: str
    status: str
    timeInForce: str
    type: str
    side: OrderSides
    workingTime: int
    fills: List[Dict]
    selfTradePreventionMode: str


class OrderStatusModel(BaseModel):
    status_code: int
    status: str
    meta: OrderMetaModel
    payload: Union[OrderPayloadModel, str]
