import courses
from django.shortcuts import render, get_object_or_404
from .models import CourseModel
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

def index(request):
    return render(request, "courses/index.html", {"courses" : CourseModel.objects.all()})

def course(request, code):
    course = CourseModel.objects.get(code=code)
    students = course.student.all()
    now = students.count()
    return render(request, "courses/course.html", {'course': course ,'students': students ,'now': now})

def takecourse(request, code):
    if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse("users:login"))

    course = CourseModel.objects.get(code=code)
    if request.user not in course.student.all():
        course.student.add(request.user)
    return HttpResponseRedirect(reverse("courses:course", args=(code,)))

def rmcourse(request, code):
    if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse("users:login"))

    course = CourseModel.objects.get(code=code)
    if request.user in course.student.all():
        course.student.remove(request.user)
    return HttpResponseRedirect(reverse("courses:course", args=(code,)))