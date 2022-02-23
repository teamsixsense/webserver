from django.db.models.query import QuerySet
from django.db.models import Q

from nst.models import Picmodel

import requests

def search(keyword: str) -> QuerySet[Picmodel]:
    result = Picmodel.objects.filter(
        Q(name__icontains=keyword)|
        Q(artist__icontains=keyword)|
        Q(desc__icontains=keyword)|
        Q(nation=keyword)
        ).distinct()
    return result


# def use_api(key, img):
#     url = "http://127.0.0.1:8001/api/v1/nsts/"
#     datas = {
#         "key":key,
#         "img":img,
#     }
#     headers = {'Content-Type':'application/json; charset=utf-8'}
#     cookies = {'ck_test': 'cookies_test'} 
#     response = requests.post(url=url, data=datas, headers=headers, cookies=cookies)
#     return response
    # pass