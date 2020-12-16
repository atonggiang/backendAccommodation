from django.urls import path, include
from . import views 
from rest_framework import routers 

router = routers.DefaultRouter()
router.register('roomlist', views.RoomViewSet, 'room')
router.register('postlist', views.PostViewSet, 'post')
router.register('userlist', views.UserViewSet, 'user')
router.register('profilelist', views.ProfileViewSet, 'profile')
router.register('reviewlist', views.ReviewViewSet, 'review')
router.register('likelist', views.LikeViewSet, 'like')
router.register('bookmarklist', views.BookmarkViewSet, 'bookmark')
router.register('commentlist', views.CommentViewSet, 'comment')
router.register('reportlist', views.ReportViewSet, 'report')
router.register('picturelist', views.PictureViewSet, 'picture')

urlpatterns = [
    path('', include(router.urls)),
]