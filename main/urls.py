from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def handler_404(*args, **kwargs):
    return JsonResponse(
        {"error": "Endpoint not found", "status_code": 404},
        status=404
    )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('users.urls')),
    path('api/posts/', include('posts.urls')),
    path('api/chats/', include('chats.urls')),
]

handler404 = 'main.urls.handler_404'