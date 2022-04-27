from django.urls import path
from message import views

urlpatterns = [
    path('messages',views.MessagesAPIView.as_view())
]