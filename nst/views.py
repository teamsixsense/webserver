from typing import Any

from asgiref.sync import async_to_sync, sync_to_async
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, View
from django.views.decorators.http import require_http_methods, require_GET

from nst.models import Picmodel
from nst.services import get_pic, search, use_api

# Create your views here.


class IndexView(TemplateView):
    template_name = "index.html"


class CategoryView(TemplateView):
    template_name = "category.html"


class PicListView(View):
    def get(self, request: HttpRequest, **kwargs: str) -> HttpResponse:
        picture_list = Picmodel.objects.filter(nation=kwargs["nation"])
        return render(request, "list.html", {"picture_list": picture_list})


async def PicDetailView(request: HttpRequest, **kwargs: int) -> HttpResponse:
    if request.method == "GET":
        picture_info = await get_pic(kwargs["pk"])
        return render(request, "detail.html", {"picture_info": picture_info})
    elif request.method == "POST":
        try:
            imgs = request.FILES["imgs"].file.getvalue() #mypy에러 왜뜨는지모름, 타입확인해야함
            url = request.POST["style_image"]
            style_image = url.split("/")[-1]

            id = await use_api(style_image=style_image, imgs=imgs)
        except:
            return redirect("detail", kwargs["pk"])
        return redirect("result", id)


class ResultView(View):
    def get(self, request: HttpRequest, **kwargs: str) -> HttpResponse:
        result = "https://d1txao2peb1gkd.cloudfront.net/" + kwargs["result"]
        return render(request, "result.html", {"result": result})


async def searchview(request: HttpRequest) -> HttpResponse:
    keyword = request.GET.get("q", None)
    if keyword:
        picture_list = await search(keyword)
        if len(picture_list) == 0:
            error = "검색 결과가 없습니다."
            return render(request, "search.html", {"picture_list": picture_list, "error": error})
        else:
            return render(request, "search.html", {"picture_list": picture_list})
    else:
        picture_list = []
        error = "검색어를 입력하세요."
        return render(request, "search.html", {"picture_list": picture_list, "error": error})
