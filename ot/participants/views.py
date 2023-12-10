from django.shortcuts import render
from .models import Competitor, Judge, Teacher
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


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
    competitor = Competitor.objects.get(slug=slug)
    return render(
        request, "participants/competitor_detail.html", {"competitor": competitor}
    )


def teacher_detail(request, slug):
    teacher = Teacher.objects.get(slug=slug)
    return render(request, "participants/teacher_detail.html", {"teacher": teacher})


def judge_detail(request, slug):
    judge = Judge.objects.get(slug=slug)
    return render(request, "participants/judge_detail.html", {"judge": judge})


def search(request):
    searched = request.GET.get("searched")
    competitors_results = Competitor.objects.filter(
        Q(first_name__icontains=searched)
        | Q(last_name__icontains=searched)
        | Q(city__icontains=searched)
        | Q(job__icontains=searched)
    )
    teachers_results = Teacher.objects.filter(
        Q(first_name__icontains=searched) | Q(last_name__icontains=searched)
    )
    judges_results = Judge.objects.filter(
        Q(first_name__icontains=searched)
        | Q(last_name__icontains=searched)
        | Q(job__icontains=searched)
    )

    results = list(competitors_results) + list(teachers_results) + list(judges_results)

    # Paginación
    page = request.GET.get("page", 1)
    paginator = Paginator(results, 5)

    try:
        paginated_results = paginator.page(page)
    except PageNotAnInteger:
        paginated_results = paginator.page(1)
    except EmptyPage:
        paginated_results = paginator.page(paginator.num_pages)
    return render(
        request, "search.html", {"results": paginated_results, "searched": searched}
    )
