from django.shortcuts import render


# Create your views here.
def portal(request):
    return render(request, '404.html')
