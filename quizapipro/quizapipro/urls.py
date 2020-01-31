from django.contrib import admin
from django.urls import path, include
from quizapiapp.api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('quizapiapp.api.urls')),
]