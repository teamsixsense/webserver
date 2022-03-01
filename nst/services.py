from datetime import datetime
from time import time
from typing import List, cast

import httpx

# import requests
from asgiref.sync import sync_to_async
from django.db.models import Q
from django.db.models.query import QuerySet

from nst.models import Picmodel


async def get_pic(pk: int) -> Picmodel:
    result = await sync_to_async(Picmodel.objects.get)(pk=pk)
    return cast(Picmodel, result)


async def search(keyword: str) -> List[Picmodel]:
    result = await sync_to_async(sync_search)(keyword)
    return cast(List[Picmodel], result)


def sync_search(keyword: str) -> List[Picmodel]:
    result = list(
        Picmodel.objects.filter(
            Q(name__icontains=keyword) | Q(artist__icontains=keyword) | Q(desc__icontains=keyword) | Q(nation=keyword)
        ).distinct()
    )
    return result


async def use_api(style_image: str, imgs) -> str:
    today = datetime.now()
    mytime = today.strftime("%Y-%m-%d-%H-%M-%S")
    data = {
        "image_name": style_image,
        "key": mytime,
    }
    files = {"img": imgs}
    async with httpx.AsyncClient() as client:
        r = await client.post("http://127.0.0.1:8001/api/v1/nsts/two", data=data, files=files)
        url = r.json()
        id = url["file_url"].split("/")[-1]
        return str(id)
