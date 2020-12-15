from django.db import models 
from django.conf import settings
from . import Post

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name='comments_user')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, related_name='comments_post')
    comment_content = models.TextField()
    is_verified = models.BooleanField(default=False)
    date_created = models.DateTimeField(verbose_name='Date Created', auto_now_add=True)
    class Meta:
        db_table = 'comment'
        ordering = ['-date_created']