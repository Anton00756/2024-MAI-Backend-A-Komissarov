"""myproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('courses', views.all_courses, name='courses'),
    path('course/<uuid:course_id>', views.course, name='course'),
    path('course/search', views.search_course, name='search_course'),
    path('course/create', views.create_course, name='create_course'),
    path('lessons', views.all_lessons, name='lessons'),
    path('lesson/<uuid:lesson_id>', views.lesson, name='lesson'),
    path('lesson/create', views.create_lesson, name='create_lesson'),
]
