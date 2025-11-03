from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('form/', views.user_form, name='user_form'),
]
