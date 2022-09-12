from django.contrib import admin
from django.urls import path

from app.views import home, send_email

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('send_email', send_email, name='send_email')
]
