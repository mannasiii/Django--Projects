from django.urls import path
from . import views

urlpatterns =[
    path('create', views.create, name='create '), #create/
    path('', views.dashboard, name='dashboard'), #dashboard
    path('edit/<sid>/', views.edit),
    path('delete/<did>/', views.delete),
]