from django.shortcuts import render


# Index Page
def index(request):
    return render(request, 'index.html')


def error_page(request):
    return render(request, '404.html')


def faculty(request):
    return render(request, 'faculty/faculty.html')


def law_base(request):
    return render(request, 'faculty/law_base.html')

