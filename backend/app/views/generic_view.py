from rest_framework import viewsets
from .. import models 
from .. import serializers 

class RoomViewSet(viewsets.ModelViewSet):
    queryset = models.Room.objects.all()
    serializer_class = serializers.RoomSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = models.Profile.objects.all()
    serializer_class = serializers.ProfileSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer

class LikeViewSet(viewsets.ModelViewSet):
    queryset = models.Like.objects.all()
    serializer_class = serializers.LikeSerializer

class BookmarkViewSet(viewsets.ModelViewSet):
    queryset = models.Bookmark.objects.all()
    serializer_class = serializers.BookmarkSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer

class ReportViewSet(viewsets.ModelViewSet):
    queryset = models.Report.objects.all()
    serializer_class = serializers.ReportSerializer

class PictureViewSet(viewsets.ModelViewSet):
    queryset = models.Picture.objects.all()
    serializer_class = serializers.PictureSerializer