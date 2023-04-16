from django.shortcuts import render
from django.http import HttpResponse

stud_db =[
    {
    'id':1,
    'name': 'Pat',
    'course': 'python',
    'score': 50,
    },
    {
    'id': 2,
    'name': 'James',
    'course': 'Html',
    'score': 60,
    },
    {
    'id': 3,
    'name': 'Sunday',
    'course': 'Js',
    'score': 80
    }
]

# Create your views here.

def hello(request, work):
    return HttpResponse('<h1>Hello Page</h1>'+ work)

def student(request, work):
    stu_info = None
    for i in stud_db:
        if i ['id'] == work:
            stu_info = i
    return render(request, 'pat/student.html', {'studs': stu_info})

def home(request):
    page ='Landing page'
    age = 22
    context = {
        'msg': page,
        'years_old': age
    }
    return render(request, 'pat/index.html', {'msg': page, 'years_old': age})

def about(request):
    return render(request, 'pat/about.html')
