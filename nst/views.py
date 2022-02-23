from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import TemplateView, View, DetailView

from nst.models import Picmodel


# Create your views here.

class IndexView(TemplateView):
    template_name = "index.html"


class CategoryView(TemplateView):
    template_name = "category.html"


class PicListView(View):
    def get(self, request, *args, **kwargs):
        picture_list = Picmodel.objects.filter(nation=kwargs["nation"])
        return render(request, "list.html", {"picture_list": picture_list})


class PicDetailView(DetailView):
    model = Picmodel
    template_name = "detail.html"
    context_object_name = "picture_info"


class ResultView(TemplateView):
    template_name = "result.html"