from django.shortcuts import render
from .models import Course
# Create your views here.

def index(request):
    return render(request, "courses/index.html", {"courses" : Course.object.all()})
    