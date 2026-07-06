from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import SignUpView, LogoutView, FollowView, BlockUserView, UpdateProfileView, UserProfileByUsernameView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/<int:pk>/follow/', FollowView.as_view(), name='follow'),
    path('users/<int:pk>/block/', BlockUserView.as_view(), name='block'),
    path('update/', UpdateProfileView.as_view(), name='update'),
    path('<str:username>/', UserProfileByUsernameView.as_view(), name='user_profile'),
]