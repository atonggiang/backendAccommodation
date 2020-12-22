from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .. import models
from .. import serializers
from .. import constants

@api_view(['PATCH'])
def approve_pending_post_action(request, pk, *args, **kwargs):
    '''
    url: approve_pending_post_action-api/<int:pk>/ (pk is post-id)
    header-authorization: user
    body: none
    '''
    post = get_object_or_404(models.Post.pending.all(), pk=pk)
    post.approve_post_status()
    return Response(status=status.HTTP_202_ACCEPTED)

@api_view(['PATCH'])
def approve_all_pending_posts_action(request, *args, **kwargs):
    '''
    url: approve_all_pending_posts_action-api/
    body: none
    '''
    posts = models.Post.pending.approve_all()
    return Response(status=status.HTTP_202_ACCEPTED)

@api_view(['GET'])
def get_approved_posts_in_effect_action(request, *args, **kwargs):
    '''
    url: get_approved_posts_in_effect_action-api/
    body: none
    '''
    posts = models.Post.approved.in_effect()
    post_json = serializers.PostSerializer(posts, many=True)
    return Response(post_json.data)

@api_view(['GET'])
def get_approved_posts_not_in_effect_action(request, *args, **kwargs):
    '''
    url: get_approved_posts_in_effect_action-api/
    body: none
    '''
    posts = models.Post.approved.not_in_effect()
    post_json = serializers.PostSerializer(posts, many=True)
    return Response(post_json.data)

@api_view(['POST'])
def create_room_action(request, *args, **kwargs):
    '''
    url: create_room_action-api/
    header-authorization: user
    body: 
        {
            <create_post_view>
        }
    '''
    request.data['user'] = request.user.id
    room_json = serializers.RoomSerializer(data=request.data)
    if room_json.is_valid():
        room_json.save()
        return Response(room_json.data, status=status.HTTP_201_CREATED)
    return Response(room_json.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
def edit_room_action(request, pk, *args, **kwargs):
    '''
    url: edit_post_action-api/<pk>/ (pk is room-id)
    header-authorization: user
    body: 
        {
            -updatefields- (no need to have user)
        }
    '''
    room = get_object_or_404(models.Room.objects.all(), pk=pk)
    request.data['user'] = room.user.id
    room_json = serializers.RoomSerializer(room, data=request.data)
    if room_json.is_valid():
        room_json.save()
        if room.post is not None:
            room.post.set_post_pending() if request.user.role == constants.OWNER else None
        return Response(room_json.data)
    return Response(room_json.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_post_action(request, pk, *args, **kwargs):
    '''
    url: create_post_action-api/<pk>/ (pk is room-id)
    body: 
        {
            <create_post_view>
        }
    '''
    room = models.Room.objects.get(pk=pk)
    request.data['verify_status'] = constants.APPROVED if room.user.role == constants.MODERATOR else constants.PENDING
    request.data['room'] = room.id
    post_json = serializers.PostSerializer(data=request.data)
    if post_json.is_valid():
        post_json.save()
        return Response(post_json.data, status=status.HTTP_201_CREATED)
    return Response(post_json.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
def edit_post_action(request, pk, *args, **kwargs):
    '''
    url: edit_post_action-api/<pk>/ (pk is post-id)
    header-authorization: user
    body: 
        {   
            -updatefields- (no need to have room)
        }
    '''
    post = get_object_or_404(models.Post.objects.all(), pk=pk)
    request.data['room'] = post.room.id
    post_json = serializers.PostSerializer(post, data=request.data)
    if post_json.is_valid():
        post_json.save()
        post.set_post_pending() if request.user.role == constants.OWNER else None
        return Response(post_json.data)
    return Response(post_json.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_profile_action(request, *args, **kwargs):
    '''
    url: create_profile_action-api/
    header-authorization: user
    body: 
        {
            <create_profile_view>
        }
    '''
    request.data['is_verified'] = True if request.user.role == constants.MODERATOR else False 
    request.data['user'] = request.user.id
    profile_json = serializers.ProfileSerializer(data=request.data)
    if profile_json.is_valid():
        profile_json.save()
        return Response(profile_json.data, status=status.HTTP_201_CREATED)
    return Response(profile_json.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
def edit_profile_action(request, pk, *args, **kwargs):
    '''
    url: edit_profile_action-api/<pk> (pk is profile-id)
    header-authorization: user
    body:
        {
            <update_profile_view>
        }
    '''
    profile = get_object_or_404(models.Profile.objects.all(), pk=pk)
    request.data['user'] = profile.user.id
    request.data['is_verified'] = True if request.user.role == constants.MODERATOR else False 
    profile_json = serializers.ProfileSerializer(profile, data=request.data)
    if profile_json.is_valid():
        profile_json.save()
        return Response(profile_json.data, status=status.HTTP_201_CREATED)
    return Response(profile_json.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_room_picture_action(request, pk, *args, **kwargs):
    '''
    url: create_room_picture_action-api/<pk>/ (pk is room-id)
    header-authorization: user
    body-formdata: {
        picture: <picture>
    }
    '''
    room = get_object_or_404(models.Room.objects.all(), pk=pk)
    request.data['room'] = room.id
    picture_json = serializers.PictureSerializer(data=request.data, context={'request':request})
    if picture_json.is_valid():
        picture_json.save()
        return Response(picture_json.data, status=status.HTTP_201_CREATED)
    return Response(profile_json.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_like_post_action(request, pk, *args, **kwargs):
    '''
    url: create_like_post_action-api/<pk> (pk is post-id)
    header-authorization: user
    '''
    post = get_object_or_404(models.Post.objects.all(), pk=pk)
    request.data['post'] = post.id
    request.data['user'] = request.user.id
    like_json = serializers.LikeSerializer(data=request.data)
    if like_json.is_valid():
        like_json.save()
        return Response(like_json.data, status=status.HTTP_201_CREATED)
    return Response(like_json.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_comment_post_action(request, pk, *args, **kwargs):
    '''
    url: create_like_post_action-api/<pk> (pk is post-id)
    header-authorization: user
    '''
    post = get_object_or_404(models.Post.objects.all(), pk=pk)
    request.data['post'] = post.id
    request.data['user'] = request.user.id
    comment_json = serializers.CommentSerializer(data=request.data)
    if comment_json.is_valid():
        comment_json.save()
        return Response(comment_json.data, status=status.HTTP_201_CREATED)
    return Response(comment_json.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_review_post_action(request, pk, *args, **kwargs):
    '''
    url: create_like_post_action-api/<pk> (pk is post-id)
    header-authorization: user
    '''
    post = get_object_or_404(models.Post.objects.all(), pk=pk)
    request.data['post'] = post.id
    request.data['user'] = request.user.id
    review_json = serializers.ReviewSerializer(data=request.data)
    if review_json.is_valid():
        review_json.save()
        return Response(review_json.data, status=status.HTTP_201_CREATED)
    return Response(review_json.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_report_post_action(request, pk, *args, **kwargs):
    '''
    url: create_like_post_action-api/<pk> (pk is post-id)
    header-authorization: user
    '''
    post = get_object_or_404(models.Post.objects.all(), pk=pk)
    request.data['post'] = post.id
    request.data['user'] = request.user.id
    report_json = serializers.ReportSerializer(data=request.data)
    if report_json.is_valid():
        report_json.save()
        return Response(report_json.data, status=status.HTTP_201_CREATED)
    return Response(report_json.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_bookmark_post_action(request, pk, *args, **kwargs):
    '''
    url: create_like_post_action-api/<pk> (pk is post-id)
    header-authorization: user
    '''
    post = get_object_or_404(models.Post.objects.all(), pk=pk)
    request.data['post'] = post.id
    request.data['user'] = request.user.id
    bookmark_json = serializers.BookmarkSerializer(data=request.data, context={'request':request})
    if bookmark_json.is_valid():
        bookmark_json.save()
        return Response(bookmark_json.data, status=status.HTTP_201_CREATED)
    return Response(bookmark_json.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_user_rooms_action(request, *args, **kwargs):
    '''
    '''
    rooms = models.Room.objects.filter(user=request.user.id)
    rooms_json = serializers.RoomSerializer(rooms, many=True, context={'request':request})
    return Response(rooms_json.data)

@api_view(['GET'])
def get_user_pending_posts_action(request, *args, **kwargs):
    '''
    '''
    posts = models.Post.pending.filter(room__user=request.user.id)
    posts_json = serializers.PostSerializer(posts, many=True, context={'request':request})
    return Response(posts_json.data)

@api_view(['GET'])
def get_user_approved_posts_action(request, *args, **kwargs):
    '''
    '''
    posts = models.Post.approved.filter(room__user=request.user.id)
    posts_json = serializers.PostSerializer(posts, many=True, context={'request':request})
    return Response(posts_json.data)

@api_view(['GET'])
def get_user_profile_action(request, *args, **kwargs):
    '''
    '''
    profile = models.Profile.objects.get(pk=request.user.profile.id)
    profile_json = serializers.ProfileSerializer(profile, context={'request':request})
    return Response(profile_json.data)

@api_view(['GET'])
def get_user_bookmarks_action(request, *args, **kwargs):
    '''
    '''
    bookmarks = models.Bookmark.objects.filter(user=request.user.id)
    bookmarks_json = serializers.BookmarkSerializer(bookmarks, many=True, context={'request':request})
    return Response(bookmarks_json.data)

@api_view(['POST'])
def login_authentication(request, *args, **kwargs):
    result = serializers.LoginSerializer(data=request.data)
    result.is_valid(raise_exception=True)
    
    user = models.User.objects.get(username=request.data['username'])
    refresh = RefreshToken.for_user(user)
    response = {
        'username': result.data['username'],
        'role' : result.data['role'],
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
    return Response(response, status=status.HTTP_200_OK)