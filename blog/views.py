from django.contrib.sitemaps.views import index
from django.shortcuts import render,redirect
from .models import Student
from .forms import StudentForm

# Create your views here.
def students_page(request):
    students = Student.objects.all()
    return render(request, 'index.html', {'students':students})

def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students_page')
    else:
        form = StudentForm

    return render(request, 'student_add.html', {'form':form})