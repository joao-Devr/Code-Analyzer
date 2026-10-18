from django.urls import path
from . import views

app_name="code_analyzer"

urlpatterns = [

    path('', views.code_analyzer, name="code_analyzer"),
]