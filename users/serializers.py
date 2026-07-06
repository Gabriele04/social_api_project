from rest_framework import serializers
from .models import SocialUser


class UserSignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = SocialUser
        fields = ('id', 'username', 'email', 'password', 'role', 'bio', 'occupation')
        read_only_fields = ('id',)

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = SocialUser.objects.create_user(**validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialUser
        fields = ('id', 'username', 'bio', 'occupation')
        read_only_fields = fields

class UpdateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)
    old_password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = SocialUser
        fields = ['username', 'email', 'bio', 'occupation', 'password', 'old_password']
    def validate_old_password(self, value):
        user = self.instance
        if not user.check_password(value):
            raise serializers.ValidationError("old password is not correct")
        return value

    def validate_email(self, value):
        user = self.instance
        if SocialUser.objects.filter(email=value).exclude(pk=user.pk).exists():
            raise serializers.ValidationError("mail already in usee")
        return value

    def update(self, instance, validated_data):
        validated_data.pop('old_password', None)
        password = validated_data.pop('password', None)
        if password:
            instance.set_password(password)
        return super().update(instance, validated_data)


