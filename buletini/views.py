from django.shortcuts import render


# Create your views here.
def scietific_bulletin(request):
    return render(request, 'scientific_bulletin.html')
