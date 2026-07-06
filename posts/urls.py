from django.urls import path
from .views import PostListCreateView, PostDetailView, LikeView, CommentCreateView, FollowedFeedView, CommentGetDeleteView

urlpatterns = [
    path('', PostListCreateView.as_view(), name='post_list_create'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('<int:pk>/like/', LikeView.as_view(), name='post_like'),
    path('feed/', FollowedFeedView.as_view(), name='personal_feed'),
    path('<int:pk>/comment/', CommentCreateView.as_view(), name='post_comment'),
    path('<int:post_pk>/comment/<int:comment_pk>/', CommentGetDeleteView.as_view(), name='post_comment_delete'),
]