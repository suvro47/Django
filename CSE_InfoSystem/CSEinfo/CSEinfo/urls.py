"""CSEinfo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Dept import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('student-list/', views.student_list, name='student-list'),
    path('teacher-list/', views.teacher_list, name='teacher-list'),
    path('staff-list/', views.staff_list, name='staff-list'),
    path('staff-list/', views.staff_list, name='staff-list'),
    path('single-student/<student_id>/', views.single_student, name='single-student'),
    path('single-teacher/<teacher_id>/', views.single_teacher, name='single-teacher'),
    path('single-staff/<staff_id>/', views.single_staff, name='single-staff'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

]
