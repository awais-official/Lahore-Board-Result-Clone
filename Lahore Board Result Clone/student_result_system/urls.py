from django.urls import path
from . import views

urlpatterns = [
    path('result/<str:roll_number>/', views.student_result_view, name='base'),
    path('',views.login)
]
