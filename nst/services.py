from django.db.models.query import QuerySet
from django.db.models import Q

from nst.models import Picmodel


def search(keyword: str) -> QuerySet[Picmodel]:
    result = Picmodel.objects.filter(
        Q(name__icontains=keyword)|
        Q(artist__icontains=keyword)|
        Q(desc__icontains=keyword)|
        Q(nation=keyword)
        ).distinct()
    return result


def use_api():
    return 