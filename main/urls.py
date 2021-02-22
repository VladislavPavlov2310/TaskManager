from django.urls import path
from . import views

urlpatterns = [
    path('', views.TaskListView.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('create/', views.TaskCreateView.as_view(), name='create'),
    path('delete/<int:pk>/', views.TaskDeleteView.as_view(), name='delete'),
    path('update/<int:pk>/', views.TaskUpdateView.as_view(), name='update'),
]
