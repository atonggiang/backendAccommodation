from django.urls import path, include
from . import views 
from rest_framework import routers 

router = routers.DefaultRouter()
router.register('postlist', views.PostViewSet, 'post')
router.register('userlist', views.UserViewSet, 'user')
router.register('profilelist', views.ProfileViewSet, 'profile')

urlpatterns = [
    path('', include(router.urls)),
]