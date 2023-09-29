from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from app.models import Classe, SessionYear, Student
from django.contrib import messages


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
        classe_id = request.POST.get('classe_id')
        join_at = request.POST.get('join_at')
        address = request.POST.get('address')
        student_pic = request.FILES.get('student_pic')
        session_year_id = request.POST.get('session_year_id')
        father_name = request.POST.get('father_name')
        father_profession = request.POST.get('father_profession')
        father_phone = request.POST.get('father_phone')
        mother_name = request.POST.get('mother_name')
        mother_profession = request.POST.get('mother_profession')
        mother_phone = request.POST.get('mother_phone')

        classe = Classe.objects.get(id=classe_id)
        session_year = SessionYear.objects.get(id=session_year_id)

        student = Student(
            first_name=first_name,
            last_name=last_name,
            gender=gender,
            dob=dob,
            level=level,
            classe_id=classe,
            date_join=join_at,
            address=address,
            picture=student_pic,
            session_id=session_year,
            father_name=father_name,
            father_profession=father_profession,
            father_phone=father_phone,
            mother_name=mother_name,
            mother_profession=mother_profession,
            mother_phone=mother_phone
        )
        student.save()
        messages.success(request, 'Nouveau Eleve Inscrit Avec Succes !')
        return redirect('add_student')

    context = {
        'classe': classe,
        'session_year': session_year
    }

    return render(request, 'Administration/add_student.html', context)