from django.urls import path
from . import views

app_name = 'bbsnote'

urlpatterns = [
    path('', views.index),
    path('<int:board_id>/', views.detail, name='detail'),
    path('comment/create/<int:board_id>/', views.comment_create, name='comment_create'),
    
]