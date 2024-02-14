from django.contrib import admin
from django.urls import path, include
from loan import views


urlpatterns = [
    path('',views.main, name='main'),
    path('loan_result',views.result, name='loan_result')
]