
from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import DetailView, TemplateView, View

from asgiref.sync import async_to_sync, sync_to_async

from nst.models import Picmodel
from nst.services import get_pic, search, sync_search

# Create your views here.


class IndexView(TemplateView):
    template_name = "index.html"


class CategoryView(TemplateView):
    template_name = "category.html"


class PicListView(View):
    def get(self, request: HttpRequest, **kwargs: str) -> HttpResponse:
        picture_list = Picmodel.objects.filter(nation=kwargs["nation"])
        return render(request, "list.html", {"picture_list": picture_list})


class PicDetailView(DetailView):  # type: ignore
    model = Picmodel
    template_name = "detail.html"
    context_object_name = "picture_info"

    def post(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        return redirect("result", kwargs["pk"])


class ResultView(View):
    def get(self, request: HttpRequest, **kwargs: int) -> HttpResponse:
        return render(request, "result.html", {"result": kwargs["result"]})


# async def ResultViewTwo(request: HttpRequest, **kwargs: Any) -> HttpResponse:
#     # a = await get_pic(2)
#     a = await search("Korea")
#     # a = sync_search("Korea")
#     print(a)
#     return render(request, "result.html", {"result": kwargs["result"]})

async def searchview(request: HttpRequest) -> HttpResponse:
    keyword = request.GET.get('q', None)
    if keyword:
        picture_list = await search(keyword)
        if len(picture_list) == 0:
            error = "검색 결과가 없습니다."
            return render(request, "search.html", {"picture_list":picture_list, "error":error})
        else:
            return render(request, "search.html", {"picture_list":picture_list})
    else:
        picture_list = []
        error = "검색어를 입력하세요."
        return render(request, "search.html", {"picture_list":picture_list, "error":error})
