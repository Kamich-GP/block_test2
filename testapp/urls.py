from django.urls import path
from . import views


urlpatterns = [
    path('', views.main_page),
    path('end', views.end_page)
]
