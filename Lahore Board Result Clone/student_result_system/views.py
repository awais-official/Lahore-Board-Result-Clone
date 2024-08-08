from django.shortcuts import render
from django.http import Http404
from .models import Student, Subject, StudentResult

def student_result_view(request, roll_number):
    try:
        student = Student.objects.get(roll_number=roll_number)
        subjects = Subject.objects.filter(student=student)
        student_result = StudentResult.objects.get(student=student)

        context = {
            'student': student,
            'subjects': subjects,
            'student_result': student_result,
        }

        return render(request, 'base.html', context)
    except Student.DoesNotExist:
        return render(request, '404.html')
    
def login(request):
    return render(request,"login2.html")