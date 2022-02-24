
from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import DetailView, TemplateView, View

from nst.models import Picmodel

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
