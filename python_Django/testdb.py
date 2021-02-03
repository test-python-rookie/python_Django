from TestMode1.models import Student
from django.shortcuts import render

# 数据库操作
def testdb(request):
    # 初始化
    response = []

    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    list = Student.objects.all()
    # 输出所有数据
    for var in list:
        response1 = []
        response1.append(var.id)
        response1.append(var.name)
        response1.append(var.sex)
        response1.append(var.age)
        response.append(response1)
    return render(request, 'runoob.html', {'response':response})