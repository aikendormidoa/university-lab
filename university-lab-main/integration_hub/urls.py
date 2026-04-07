from django.urls import path
from .views import get_student_report

urlpatterns = [
    path('report/<str:student_id>/', get_student_report),
]