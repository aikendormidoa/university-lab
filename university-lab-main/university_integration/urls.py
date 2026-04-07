from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/students/', include('student_app.urls')),
    path('api/library/', include('library_app.urls')),
    path('api/payments/', include('payment_app.urls')),
    path('api/hub/', include('integration_hub.urls')),
]