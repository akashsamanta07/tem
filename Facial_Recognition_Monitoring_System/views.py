from django.shortcuts import render


def home(request):
    return render(request,"index.html")

def student_login(request):
    return render(request,"student_login.html")



def teacher_login(request):
    return render(request,"teacher_login.html")


def admin_login(request):
    return render(request,"admin_login.html")