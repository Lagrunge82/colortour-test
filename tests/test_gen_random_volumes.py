from typing import List, Dict
from utils import gen_random_volumes
from src.enums.global_enums import GlobalErrorMessages


def test_volumes():
    tests: List = [
        {
            'cases_quantity': 100,
            'total_volume': 10000,
            'quantity': 5,
            'spread': 50,
        },
        {
            'cases_quantity': 50,
            'total_volume': 50000,
            'quantity': 10,
            'spread': 70,
        },
    ]

    for test in tests:
        for _ in range(test['cases_quantity']):
            volumes: List[float] = gen_random_volumes(volume=test["total_volume"],
                                                      quantity=test["quantity"],
                                                      amountDif=test["spread"])

            assert len(volumes) == test["quantity"], \
                GlobalErrorMessages.ORDERS_COUNT_ERROR.value
            assert round(sum(volumes), 2) == test["total_volume"], \
                GlobalErrorMessages.ORDERS_SUM_ERROR.value

            min_vlm: float = (test["total_volume"] / test["quantity"] - test["spread"])
            max_vlm: float = (test["total_volume"] / test["quantity"] + test["spread"])
            min_vlm_er: bool = min(volumes) < min_vlm
            max_vlm_er: bool = max(volumes) > max_vlm
            #
            if min_vlm_er or max_vlm_er:
                print(
                    f'\nmin_vlm: {min(volumes)} vs {min_vlm}',
                    f'\nmax_vlm: {max(volumes)} vs {max_vlm}',
                    '\nresult:', volumes
                )
            assert (min(volumes) < min_vlm) is False and (max(volumes) > max_vlm) is False, \
                GlobalErrorMessages.ORDERS_VOLUME_ERROR.value
