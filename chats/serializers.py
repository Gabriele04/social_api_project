from rest_framework import serializers
from .models import Message

class MessageSerializer(serializers.ModelSerializer):
    sender_username = serializers.ReadOnlyField(source='sender.username')
    receiver_username = serializers.ReadOnlyField(source='receiver.username')

    class Meta:
        model = Message
        fields = ('id', 'sender', 'sender_username', 'receiver','receiver_username', 'body', 'sent_at')
        read_only_fields = ('sender', 'receiver', 'sent_at')