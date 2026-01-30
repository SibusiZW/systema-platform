from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.signout, name='logout'),
    path('machines/', views.machine_list, name='machines'),
    path('add_machine/', views.add_machine, name='add_pc'),
    path('delete/<int:id>/', views.delete_pc, name='delete'),
]