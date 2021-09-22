from django.shortcuts import render


# Create your views here.
def biology_department(request):
    return render(request, 'departments/biology_department.html')


def biotechnology_department(request):
    return render(request, 'departments/biotechnology_department.html')


def physic_department(request):
    return render(request, 'departments/physic_department.html')


def informatic_department(request):
    return render(request, 'departments/informatic_department.html')


def chemistry_department(request):
    return render(request, 'departments/chemistry_department.html')


def industrial_chemistry_department(request):
    return render(request, 'departments/industrial_chemistry_department.html')


def mathematic_department(request):
    return render(request, 'departments/math_department.html')


def applied_mathematic_department(request):
    return render(request, 'departments/applied_math_department.html')


def search_center_flora_and_fauna_department(request):
    return render(request, 'departments/search_center_flora_and_fauna_department.html')


def projects(request):
    return render(request, 'scientific_research/projects.html')


def publications_and_conferences(request):
    return render(request, 'scientific_research/publications_and_conferences.html')


def doctoratures(request):
    return render(request, 'scientific_research/doctoratures.html')


def elearning(request):
    return  render(request, 'departments/elearning.html')


def academic(request):
    return  render(request, 'departments/academic.html')
