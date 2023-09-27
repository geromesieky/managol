from django.contrib import admin
from .models import CustomUser, Classe, Course, SessionYear, Student, Professor
from django.contrib.auth.admin import UserAdmin


# Register your models here.
class UserModel(UserAdmin):
    list_display = ['username', 'user_type']


@admin.register(Classe)
class ClasseModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'level', 'cost', 'total']


@admin.register(Course)
class CourseModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'prof_id']


@admin.register(SessionYear)
class SessionYearModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'session_start', 'session_end']


@admin.register(Student)
class StudentModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'dob', 'gender', 'level', 'picture', 'date_join']


@admin.register(Professor)
class ProfessorModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'courses', 'picture', 'date_join']


admin.site.register(CustomUser, UserModel)
