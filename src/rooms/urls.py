from django.urls import path

from . import views

urlpatterns = [
    path('<int:pk>/', views.RoomDetailView.as_view(), name='detail'),
    path('', views.RoomCreateView.as_view(), name='new'),
]

app_name = 'rooms'
