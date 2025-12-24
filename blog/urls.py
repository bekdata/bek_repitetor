from django.urls import path
from .views import students_page, student_create

urlpatterns = [
    path('', students_page, name = 'students_page'),
    path('add/', student_create, name = 'student_create'),
]