from django.urls import path
from .views import ChatHistoryView, SendMessageView

urlpatterns = [
    path('history/<int:user2>/', ChatHistoryView.as_view(), name='chat_history'),
    path('send/<int:pk>/', SendMessageView.as_view(), name='send_message'),
]