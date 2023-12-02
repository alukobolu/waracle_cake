from django.urls import path, include
from . import views
# app_name = "main_api"

urlpatterns = [
    path('cakes', views.CakeView.as_view(), name='cakes')
]