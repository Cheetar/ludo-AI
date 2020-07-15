from django.db import models
from django.conf import settings

class Code(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,)
    title = models.CharField(max_length=200)
    code = models.CharField(max_length=20000)
    rating = models.IntegerField(default=1200)

    def __str__(self):
        return self.title
