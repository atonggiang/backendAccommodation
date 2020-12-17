from django.db import models
from .. import constants

class PendingPost(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(verify_status=constants.PENDING)

class ApprovedPost(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(verify_status=constants.APPROVED)
    def approve_all(self):
        posts = self.get_queryset()
        for post in posts:
            post.approve_post_status()
    def in_effect(self):
        posts =  self.get_queryset()
        result = []
        for post in posts:
            result.append(post) if not post.is_due() else post.set_post_pending()
        return result

class DeclinedPost(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(verify_status=constants.DECLINED)