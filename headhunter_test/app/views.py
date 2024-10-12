from django.shortcuts import render


def login(request):
    return render(request, 'login.html')


def questions(request):
    return render(request, 'questions.html')


def results(request):
    return render(request, 'results.html')