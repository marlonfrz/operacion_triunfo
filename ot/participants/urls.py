from django.urls import path

from . import views

urlpatterns = [
    path("competitors_list/", views.competitors_list, name="competitors_list"),
    path("judges_list/", views.judges_list, name="judges_list"),
    path("teachers_list/", views.teachers_list, name="teachers_list"),
    path("", views.main, name="main"),
]
