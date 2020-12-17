from django.urls import path, include
from . import views 
from rest_framework import routers 

router_generic = routers.DefaultRouter()
router_generic.register('room-list', views.RoomViewSet, 'room')
router_generic.register('post-list', views.PostViewSet, 'post')
router_generic.register('user-list', views.UserViewSet, 'user')
router_generic.register('profile-list', views.ProfileViewSet, 'profile')
router_generic.register('review-list', views.ReviewViewSet, 'review')
router_generic.register('like-list', views.LikeViewSet, 'like')
router_generic.register('bookmark-list', views.BookmarkViewSet, 'bookmark')
router_generic.register('comment-list', views.CommentViewSet, 'comment')
router_generic.register('report-list', views.ReportViewSet, 'report')
router_generic.register('picture-list', views.PictureViewSet, 'picture')

post_router = routers.DefaultRouter()
post_router.register('pending-list', views.PendingPostViewSet, 'pending')
post_router.register('approved-list', views.ApprovedPostViewSet, 'approved')
post_router.register('declined-list', views.DeclinedPostViewSet, 'declined')

user_router = routers.DefaultRouter()
user_router.register('moder-list', views.ModeratorViewSet, 'moder')
user_router.register('owner-list', views.OwnerViewSet, 'owner')
user_router.register('renter-list', views.RenterViewSet, 'renter')

profile_router = routers.DefaultRouter()
profile_router.register('verified-list', views.ProfileVerifiedViewSet, 'verified')
profile_router.register('notverified-list', views.ProfileNotVerifiedViewSet, 'notverified')

urlpatterns = [
    path('generic-api/', include(router_generic.urls)),
    path('post-api/', include(post_router.urls)),
    path('user-api/', include(user_router.urls)),
    path('profile-api/', include(profile_router.urls)),
]