from django.shortcuts import render


def main(request):
    return render(request, "main.html")


def competitors_list(request):
    return render(request, "participants/competitors_list.html")


def judges_list(request):
    return render(request, "participants/judges_list.html")


def teachers_list(request):
    return render(request, "participants/teachers_list.html")
