from django.urls import path
from . import views, testdb, regiest

# urlpatterns = [
#     path('demo/', views.demo),
# ]

urlpatterns = [
    # path('demo/', views.runoob),
    path('testdb/', testdb.testdb),
    path('regiest/', regiest.regiest),
    path('regiest-form/', regiest.regiest_from),
]

