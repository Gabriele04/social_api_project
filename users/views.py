from rest_framework import generics, permissions, status
from .models import SocialUser
from .serializers import UserSignUpSerializer, UpdateSerializer, UserProfileSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken


class SignUpView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = SocialUser.objects.all()
    serializer_class = UserSignUpSerializer

class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        try:
            refresh_token = request.data['refresh']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "logout successfull"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": "missing token or not valid"}, status=status.HTTP_400_BAD_REQUEST)

class FollowView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        user = generics.get_object_or_404(SocialUser, pk=pk)
        current_user = request.user

        if current_user == user:
            return Response({"message": "you cannot follow your self"}, status=status.HTTP_400_BAD_REQUEST)

        if user in current_user.following.all():
            current_user.following.remove(user)
            return Response({"message": f"stopped to follow {user.username}"}, status=status.HTTP_200_OK)
        else:
            current_user.following.add(user)
            return Response(
                {"message": f"started to follow {user.username}"}, status=status.HTTP_200_OK)

class BlockUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        if request.user.role != 'moderator':
            return Response({"message": "you don't have moderator permissions"}, status=status.HTTP_403_FORBIDDEN)

        user = generics.get_object_or_404(SocialUser, pk=pk)

        if request.user == user:
            return Response({"message": "you can't block your self"}, status=status.HTTP_403_FORBIDDEN)
        elif user.role == 'moderator':
            return Response({"message": "you can't block a moderator"}, status=status.HTTP_403_FORBIDDEN)

        if user.is_active:
            user.is_active = False
            user.save()
            return Response({"message": "user blocked"}, status=status.HTTP_200_OK)
        else:
            user.is_active = True
            user.save()
            return Response({"message": "user unblocked"}, status=status.HTTP_200_OK)

class UpdateProfileView(generics.UpdateAPIView):
    serializer_class = UpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

class UserProfileByUsernameView(generics.RetrieveAPIView):
    queryset = SocialUser.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'username'