from django.urls import path
from .views import (AllCreateToDoView,GetToDoByUserView,DetailUpdateDeleteToDoView,
                    StatusUpdateView,GetToDosByStatusView)

urlpatterns = [
    path('',AllCreateToDoView.as_view()),
    path('gettodobyuser/',GetToDoByUserView.as_view()),
    path('status/<int:task_id>/',StatusUpdateView.as_view()),
    path('done/<str:status_type>/',GetToDosByStatusView.as_view()),
    path('<pk>/',DetailUpdateDeleteToDoView.as_view()),
]
