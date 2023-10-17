from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('post', views.PostViewSet, basename='post')

urlpatterns = [
    path('', include(router.urls)), # 게시글 뷰
    path('register/', views.RegisterAPIView.as_view()), # 회원가입 뷰
    path("auth/", views.AuthAPIView.as_view()), # post - 로그인, delete - 로그아웃, get - 유저정보
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

