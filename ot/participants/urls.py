from django.urls import path

from . import views

urlpatterns = [
    path("competitors_list/", views.competitors_list, name="competitors_list"),
    path("judges_list/", views.judges_list, name="judges_list"),
    path("teachers_list/", views.teachers_list, name="teachers_list"),
    path(
        "competitor_detail/<slug:slug>",
        views.competitor_detail,
        name="competitor_detail",
    ),
    path(
        "teacher_detail/<slug:slug>",
        views.teacher_detail,
        name="teacher_detail",
    ),
    path(
        "judge_detail/<slug:slug>",
        views.judge_detail,
        name="judge_detail",
    ),
    path("search/", views.search, name="search"),
    path("", views.main, name="main"),
]
