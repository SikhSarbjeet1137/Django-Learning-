from django.urls import path
from . import views

urlpatterns=[
    path('', views.home,name='home'),
    path('hello/<str:name>/', views.hello, name='hello'),
    path('about/',views.about,name='about'),
    path('status/', views.status_check, name='status_check'),
    path('student/<int:student_id>/',views.student_details,name='student_details')
]