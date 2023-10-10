from django.shortcuts import render, redirect

from .models import Student
from .forms import StudentForm

def new(request):
    # 새로운 student 를 생성하기 위한 <form>(HTML) => 작성데이터는 create 함수로 보내야 함
    form = StudentForm()
    return render(request, 'crud/new.html', {
        'form': form,
    })


def create(request):
    # new.html 에서 넘어온 데이터를 실제 저장
    form = StudentForm(data=request.POST)
    if form.is_valid():
        student = form.save()
        return redirect('crud:detail', student.pk)
    else:
        return render(request, 'crud/new.html', {
            'form': form,
        })
    

def index(request):
    # 전체 학생 목록 확인
    students = Student.objects.all()
    return render(request, 'crud/index.html', {
        'students': students,
    })


def detail(request, pk):
    # 학생 상세 정보 확인
    student = Student.objects.get(pk=pk)
    return render(request, 'crud/detail.html', {
        'student': student,
    })


def edit(request, pk):
    # student 를 수정하기 위한 <form>(HTML) => 작성데이터는 update 함수로 보내야 함
    student = Student.objects.get(pk=pk)
    form = StudentForm(instance=student)

    return render(request, 'crud/edit.html', {
        'student': student,
        'form': form,
    })


def update(request, pk):
    # edit.html 에서 넘어온 데이터를 실제 저장
    student = Student.objects.get(pk=pk)
    form = StudentForm(data=request.POST, instance=student)
    if form.is_valid():
        student = form.save()
        return redirect('crud:detail', student.pk)
    else:
        return render(request, 'crud/new.html', {
            'form': form,
            'student': student,
        })
    



def delete(request, pk):
    # URL 에 넘어온 pk 에 해당하는 학생정보 삭제
    student = Student.objects.get(pk=pk)
    student.delete()
    # view 에서 redirect => '<app_name>:<name>'
    return redirect('crud:index')

    # DTL(템플릿)  {% url '<app_name>:<name>' %}