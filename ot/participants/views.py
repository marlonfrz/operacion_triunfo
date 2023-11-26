from django.shortcuts import render
from .models import Competitor, Judge, Teacher


def main(request):
    return render(request, "main.html")


def competitors_list(request):
    competitors = Competitor.objects.all()
    return render(
        request, "participants/competitors_list.html", {"competitors": competitors}
    )


def judges_list(request):
    judges = Judge.objects.all()
    return render(request, "participants/judges_list.html", {"judges": judges})


def teachers_list(request):
    teachers = Teacher.objects.all()
    return render(request, "participants/teachers_list.html", {"teachers": teachers})


def competitor_detail(request, slug):
    slug = Competitor.objects.get(slug=slug)
    return render(request, "participants/competitor_detail.html", {"slug": slug})
