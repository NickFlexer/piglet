from django.urls import path

from .views import ListTask, DetailTask


urlpatterns = [
    path('<int:pk>/', DetailTask.as_view()),
    path('', ListTask.as_view()),
]
