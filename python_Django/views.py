from django.shortcuts import render
from . import testdb

def runoob(request):
    response = testdb.testdb
    return render(request, 'runoob.html', {'response':response})
