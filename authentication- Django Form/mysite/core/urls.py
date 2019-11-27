from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    # path('login/', views.login, name='login'),   we are using the django login views
    # path('logout/', views.logout, name='logout'),  we are using the django logout views
]
