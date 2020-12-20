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
    path('approve_pending_post_action-api/<int:pk>/', views.approve_pending_post_action),
    path('approve_all_pending_posts_action-api/', views.approve_all_pending_posts_action),
    path('get_approved_posts_in_effect_action-api/', views.get_approved_posts_in_effect_action),
    path('get_approved_posts_not_in_effect_action-api/', views.get_approved_posts_not_in_effect_action),
    path('create_room_action-api/', views.create_room_action),
    path('edit_room_action-api/<int:pk>/', views.edit_room_action),
    path('create_post_action-api/<int:pk>/', views.create_post_action),
    path('edit_post_action-api/<int:pk>/', views.edit_post_action),
    path('create_profile_action-api/', views.create_profile_action),
    path('edit_profile_action-api/<int:pk>/', views.edit_profile_action),
    path('create_room_picture_action-api/<int:pk>/', views.create_room_picture_action),
    path('create_like_post_action-api/<int:pk>/', views.create_like_post_action),
    path('create_comment_post_action-api/<int:pk>/', views.create_comment_post_action),
    path('create_review_post_action-api/<int:pk>/', views.create_review_post_action),
    path('create_report_post_action-api/<int:pk>/', views.create_report_post_action),
    path('create_bookmark_post_action-api/<int:pk>/', views.create_bookmark_post_action),
    path('get_user_rooms_action-api/', views.get_user_rooms_action),
    path('get_user_pending_posts_action-api/', views.get_user_pending_posts_action),
    path('get_user_approved_posts_action-api/', views.get_user_approved_posts_action),
    path('get_user_profile_action-api/', views.get_user_profile_action),
    path('get_user_bookmarks_action-api/', views.get_user_bookmarks_action),
    path('login_authentication-api/', views.login_authentication),
]