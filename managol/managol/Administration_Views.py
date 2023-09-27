from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from app.models import Classe, SessionYear


@login_required(login_url='/')
def home(request):
    return render(request, 'Administration/home.html')


@login_required(login_url='/')
def add_student(request):
    classe = Classe.objects.all()
    session_year = SessionYear.objects.all()

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        level = request.POST.get('level')
        classe_name = request.POST.get('classe_name')
        join_at = request.POST.get('join_at')
        address = request.POST.get('address')
        student_pic = request.POST.get('student_pic')
        session_year_id = request.POST.get('session_year_id')
        father_name = request.POST.get('father_name')
        father_profession = request.POST.get('father_profession')
        father_phone = request.POST.get('father_phone')
        mother_name = request.POST.get('mother_name')
        mother_profession = request.POST.get('mother_profession')
        mother_telephone = request.POST.get('mother_telephone')

    context = {
        'classe': classe,
        'session_year': session_year
    }

    return render(request, 'Administration/add_student.html', context)
