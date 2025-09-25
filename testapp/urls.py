from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page),
    path('test-time/<str:pk>', views.test_time),
    path('end', views.end_page)
]
