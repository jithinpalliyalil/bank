from django.urls import path
from .import views

urlpatterns = [

    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('customer_form', views.Customer_forms, name='customer_form'),
    path('branches', views.branches, name = 'branches'),
    path('logout', views.logout, name = 'logout'),
]
