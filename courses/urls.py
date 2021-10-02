from django.urls import path
from . import views
from .models import CourseModel

app_name="courses"
urlpatterns =[
    path('', views.index, name="index"),
    path('<str:code>', views.course, name="course"),
    path('<str:code>/takecourse', views.takecourse, name="takecourse"),
    path('<str:code>/rmcourse', views.rmcourse, name="rmcourse"),
    ]