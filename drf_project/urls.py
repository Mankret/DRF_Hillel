from django.urls import path, include
from rest_framework.routers import DefaultRouter
from drf_project import views


router = DefaultRouter()
router.register(r'users', views.UserViewSet, basename="user")
router.register(r'posts', views.PostViewSet, basename="post")
router.register(r'comments', views.CommentViewSet, basename="comment")


urlpatterns = [
    path('', include(router.urls)),
]

