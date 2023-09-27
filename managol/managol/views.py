from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponse
from app.EmailBackend import EmailBackend
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from app.models import CustomUser


def base(request):
    return render(request, 'base.html')


def user_login(request):
    return render(request, 'login.html')


def do_login(request):
    if request.method == 'POST':
        user = EmailBackend.authenticate(request,
                                         username=request.POST.get('email'),
                                         password=request.POST.get('password'))
        if user is not None:
            login(request, user)
            user_type = user.user_type
            if user_type == '1':
                return redirect('administration_home')
            elif user_type == '2':
                return HttpResponse('This Staff panel')
            elif user_type == '3':
                return HttpResponse('This Student panel')
            else:
                messages.error(request, 'Email et mot de passe incorrect !')
                return redirect('login')
        else:
            messages.error(request, 'Email et mot de passe incorrect !')
            return redirect('login')


def do_logout(request):
    logout(request)
    return redirect('login')


@login_required(login_url='/')
def profile(request):
    user = CustomUser.objects.get(id=request.user.id)

    context = {
        'user': user
    }
    return render(request, 'profile.html', context)


@login_required(login_url='/')
def profile_update(request):
    if request.method == 'POST':
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            custom_user = CustomUser.objects.get(id=request.user.id)

            custom_user.first_name = first_name
            custom_user.last_name = last_name

            if password is not None and password != "":
                custom_user.set_password(password)
            if profile_pic is not None and profile_pic != "":
                custom_user.profile_pic = profile_pic
            custom_user.save()
            messages.success(request, 'Votre profile a ete mis a jour avec succes.')
            return redirect('profile')
        except:
            messages.error(request, 'Echec de mis a jour du profile.')

    return render(request, 'profile.html')
