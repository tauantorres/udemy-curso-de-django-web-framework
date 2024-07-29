
from django.shortcuts import render

from django.http import HttpResponse


# Create your views here.
def home(request) -> HttpResponse:
    return render(
        request=request, 
        template_name='recipes/pages/home.html',
    )

def recipe(request, id) -> HttpResponse:
    return render(
        request=request, 
        template_name='recipes/pages/home.html',
    )

