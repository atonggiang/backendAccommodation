from django.db import models 
from django.conf import settings
from . import Post

class Report(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name='reports_user')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, related_name='reports_post')
    report_content = models.TextField()
    date_created = models.DateTimeField(verbose_name='Date Created', auto_now_add=True)
    class Meta:
        db_table = 'report'
        ordering = ['-date_created']
        unique_together = [['post', 'user'],]