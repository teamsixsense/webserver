from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from nst.models import Picmodel


# Create your views here.

class IndexView(TemplateView):
    template_name = "index.html"


class CategoryView(TemplateView):
    template_name = "category.html"


class PicListView(ListView):
    template_name = "list.html"
    context_object_name = "picture_list"

    def get_queryset(self) -> QuerySet[Picmodel]:
        return Picmodel.objects.filter()


class PicDetailView(DetailView):
    template_name = "detail.html"


class ResultView(TemplateView):
    template_name = "result.html"