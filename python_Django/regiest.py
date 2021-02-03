from django.shortcuts import render
from TestMode1.models import Student
from . import testdb

# 表单
def regiest_from(request):
    return render(request, 'regiest.html')

# 接收请求
def regiest(request):
    request.encoding = 'utf-8'
    id = request.GET.get('id')
    name = request.GET.get('name')
    sex = request.GET.get('sex')
    age = request.GET.get('age')
    stu = Student(id = id, name = name, sex = sex, age = age)
    stu.save()