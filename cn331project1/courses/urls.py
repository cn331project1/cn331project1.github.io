from django.urls import path
from . import views
from .models import Course

app_name="courses"
urlpatterns =[
    path('', views.index, name="index"),
    path('<str:code>', views.course, name="course"),
    ]