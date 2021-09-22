from django.shortcuts import render


# Create your views here.
def student(request):
    context = {}
    return render(request, 'student/student.html', context)


def notifications(request):
    context = {}
    return render(request, 'student/notifications.html', context)


def burses(request):
    context = {}
    return render(request, 'student/burses.html', context)
