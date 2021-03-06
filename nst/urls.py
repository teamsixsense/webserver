from django.urls import path

from nst import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("category/", views.CategoryView.as_view(), name="category"),
    path("category/<str:nation>", views.PicListView.as_view(), name="list"),
    path("detail/<int:pk>", views.PicDetailView, name="detail"),
    path("result/<str:result>", views.ResultView.as_view(), name="result"),
    path("search/", views.searchview, name="search"),  # type: ignore
]
