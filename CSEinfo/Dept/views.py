from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .models import Student
from .models import Teacher
from .models import Staff


def home(request):
    return render(request, 'home.html')


def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'student_list': students})


def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'teacher_list.html', {'teacher_list': teachers})


def staff_list(request):
    staffs = Staff.objects.all()
    return render(request, 'staff_list.html', {'staff_list': staffs})


def single_student(request, student_id):
    student = Student.objects.get(pk=student_id)
    return render(request, 'single_student.html', {'student': student})


def single_teacher(request, teacher_id):
    teacher = Teacher.objects.get(pk=teacher_id)
    return render(request, 'single_teacher.html', {'teacher': teacher})


def single_staff(request, staff_id):
    staff = Staff.objects.get(pk=staff_id)
    return render(request, 'single_staff.html', {'staff': staff})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return render(request, 'welcome.html')
        else:
            return HttpResponse("Username or Password incorrect")
    else:
        return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login')

