from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginAPIView.as_view(), name='login'),
    path('now/', views.NowAPIView.as_view(), name='now'),
    path('stats/', views.StatsAPIView.as_view(), name='stats'),
]