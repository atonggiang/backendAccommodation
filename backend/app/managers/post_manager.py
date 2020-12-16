from django.db import models

class PostQuerySetByStatus(models.QuerySet):
    def pending(self):
        return self.filter(verify_status='P')

    def approved(self):
        return self.filter(verify_status='A')

    def declined(self):
        return self.filter(verify_status='A')

class PostMangager(models.Model):
    def get_queryset(self):
        return PostQuerySetByStatus(self.model, using=self._db)

    def pending(self):
        return self.get_queryset().pending()

    def approved(self):
        return self.get_queryset().approved()

    def declined(self):
        return self.get_queryset().declined()