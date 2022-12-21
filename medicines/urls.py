from django.urls import path
from medicines.views import category_list_view, category_detail_view, detail_medicine_view, home

urlpatterns = [
    path("category/", category_list_view, name="category-list"),
    path("category/<int:id>/", category_detail_view, name="category-detail"),
    path("medicine/<int:id>/", detail_medicine_view, name="medicine-detail"),
    path("", home, name="home"),
]




