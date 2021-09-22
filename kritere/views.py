from django.shortcuts import render


# Create your views here.
def criteres_and_quotes(request):
    return render(request, 'events/criteres_and_quotes.html')
