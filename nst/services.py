from typing import List, cast
from time import time
from django.db.models.query import QuerySet
from django.db.models import Q

from asgiref.sync import sync_to_async

from nst.models import Picmodel

import requests


async def get_pic(pk:int) -> Picmodel:
    result = await sync_to_async(Picmodel.objects.get)(pk=pk)
    return cast(Picmodel, result)


async def search(keyword: str) -> List[Picmodel]:
    result = await sync_to_async(sync_search)(keyword)
    return cast(List[Picmodel], result)


def sync_search(keyword: str) -> List[Picmodel]:
    result = list(Picmodel.objects.filter(
        Q(name__icontains=keyword)|
        Q(artist__icontains=keyword)|
        Q(desc__icontains=keyword)|
        Q(nation=keyword)
        ).distinct())
    return result


# def use_api(key, img):
#     url = "http://127.0.0.1:8001/api/v1/nsts/"
#     datas = {
#         "key":key,
#         "img":img,
#     }
#     response = requests.post(url=url, data=datas)
#     return response
