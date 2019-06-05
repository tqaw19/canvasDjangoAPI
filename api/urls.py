from django.urls import path
from . import views

urlpatterns = [
    path('courses/', views.courses, name ='courses'),
    path('courses/<str:course_id>/students', views.students, name ='students'),
    path('courses/<str:course_id>/enrollments', views.enrollments, name ='enrollments'),
    path('courses/<str:course_id>/assignments', views.assignments, name ='assignments'),
    path('users/<str:user_id>/enrollments', views.users, name ='users'),
    #path('accounts/<str:account_id>/enrollments/<str:id>', views.enrollment_byid, name ='enrollment_byid'),
    
]