import random
import numpy as np
from typing import List, Optional


def gen_random_volumes(volume: float, quantity: int, amountDif: float) -> List:
    if not isinstance(quantity, int):
        raise TypeError('...')
    if quantity < 1:
        raise ValueError('...')
    # минимально допустимый объём ордера
    min_allowed_vlm: Optional[float] = 1.0
    # максимально допустимый объём ордера
    max_allowed_vlm: Optional[float] = None
    result: List[float] = []
    # средний объём открываемых ордеров
    avg_vlm: float = round(volume / quantity, 2)
    # нижняя граница объёма открываемых ордеров
    min_vlm: float = avg_vlm - round(amountDif, 2) \
        if min_allowed_vlm is None else max(avg_vlm - round(amountDif, 2), min_allowed_vlm)
    # верхняя граница объёма открываемых ордеров
    max_vlm: float = avg_vlm + round(amountDif, 2) \
        if max_allowed_vlm is None else min(avg_vlm - round(amountDif, 2), max_allowed_vlm)
    # список отклонений объёмов открываемых ордеров от среднего объёма
    diffs: List[float] = []

    for _ in range(quantity - 1):
        order_vlm: float = round(random.uniform(min_vlm, max_vlm), 2)
        order_diff: float = order_vlm - avg_vlm
        avg_diff: float = sum(diffs) + order_diff
        adjust_val = random.uniform(min(avg_diff + 50, 50),
                                      max(avg_diff - 50, -50)) if abs(avg_diff) > 50 else 0
        order_vlm -= round(adjust_val, 2)
        diffs.append(float(np.around(order_vlm - avg_vlm)))
        result.append(float(np.around(order_vlm, 2)))
        volume -= order_vlm

    if volume < min_vlm:
        diff = min_vlm - volume
        result[result.index(max(result))] = float(np.around(result[result.index(max(result))] - diff, 2))
        volume += float(np.around(diff, 2))
    if volume > max_vlm:
        diff = max_vlm - volume
        result[result.index(min(result))] = float(np.around(result[result.index(min(result))] - diff, 2))
        volume += float(np.around(diff, 2))

    result.append(float(np.around(volume, 2)))
    return result


if __name__ == '__main__':
    total = 10000
    num_parts = 5
    spread = 50
    for _ in range(10):
        volumes = gen_random_volumes(total, num_parts, spread)
        print(min(volumes) < (total / num_parts - spread),
              max(volumes) > (total / num_parts + spread),
              volumes,
              round(sum(volumes), 2))
