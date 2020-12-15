from django.db import models 
from django.conf import settings
from . import Post

class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name='reviews_user')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, related_name='reviews_post')
    review_content = models.TextField()
    VERY_BAD = 'VB'
    BAD = 'B'
    MEDIUM = 'M'
    GOOD = 'G'
    VERY_GOOD = 'VG'
    RATING_TYPE = [
        (VERY_BAD, 'Very Bad'),
        (BAD, 'Bad'),
        (MEDIUM, 'Medium'),
        (GOOD, 'Good'),
        (VERY_GOOD, 'Very Good'),
    ]
    rating = models.CharField(max_length=2, choices=RATING_TYPE, default=MEDIUM)
    is_verified = models.BooleanField(default=False)
    date_created = models.DateTimeField(verbose_name='Date Posted', auto_now_add=True)
    class Meta:
        db_table = 'review'
        ordering = ['-date_created']
        unique_together = [['post', 'user'],]