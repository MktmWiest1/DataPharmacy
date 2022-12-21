from django.shortcuts import render
from django.http import HttpResponse
from medicines.models import Category, Medicine


def category_list_view(request):
    context = {
        "category": Category.objects.all()
        }
    return render(request, "category_list.html", context)


def category_detail_view(request, **kwargs):
    category = Category.objects.get(id=kwargs["id"])
    medicines = Medicine.objects.filter(category_id=category)
    context = {
        "category": category,
        "medicines": medicines
    }
    return render(request, "category_detail.html", context)


def detail_medicine_view(request, **kwargs):
    medicine = Medicine.objects.get(id=kwargs["id"])
    return render(request, "medicine_detail.html", context={
        "medicine": medicine
        })


def home(request):
    return render(request, "index.html")

