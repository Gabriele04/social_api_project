from rest_framework import generics, permissions
from django.db.models import Q
from .models import Message
from .serializers import MessageSerializer

class ChatHistoryView(generics.ListAPIView):
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        user2 = self.kwargs['user2']

        return Message.objects.filter(
            Q(sender=user, receiver_id=user2) |
            Q(sender_id=user2, receiver=user)
        )

class SendMessageView(generics.CreateAPIView):
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        receiver = self.kwargs.get('pk')
        serializer.save(sender=self.request.user, receiver_id=receiver)