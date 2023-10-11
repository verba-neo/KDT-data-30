from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST, require_safe

from .models import Student
from .forms import StudentForm


@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = StudentForm(data=request.POST)
        if form.is_valid():
            student = form.save()
            return redirect('crud:detail', student.pk)
    else:
        form = StudentForm()
    
    return render(request, 'crud/form.html', {
        'form': form,
    })
    

@require_safe
def index(request):
    # 전체 학생 목록 확인
    students = Student.objects.all()
    return render(request, 'crud/index.html', {
        'students': students,
    })


@require_safe
def detail(request, pk):
    # 학생 상세 정보 확인
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'crud/detail.html', {
        'student': student,
    })


@require_http_methods(['GET', 'POST'])
def update(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == 'POST':
        form = StudentForm(data=request.POST, instance=student)
        if form.is_valid():
            student = form.save()
            return redirect('crud:detail', student.pk)
    else:
        form = StudentForm(instance=student)

    return render(request, 'crud/form.html', {
        'form': form,
    })
    
@require_POST
def delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return redirect('crud:index')
