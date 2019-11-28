from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('user-list/', views.user_list, name='user-list'),
    path('register/', views.register, name='register'),
    path('single-user/<user_id>/', views.single_user, name='single-user'),
    # path('login/', views.login, name='login'),   we are using the django login views
    # path('logout/', views.logout, name='logout'),  we are using the django logout views
]
