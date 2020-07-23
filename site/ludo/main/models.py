from django.db import models
from django.conf import settings
from trueskill import Rating

class Code(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,)
    title = models.CharField(max_length=200)
    code = models.CharField(max_length=20000)
    #rating = Rating()
    public = models.BooleanField(default=True)

    #type
    #no round

    #class Meta:
    #    order_with_respect_to = 'rating'

    def __str__(self):
        return self.title

    '''
    def set_title(self, t): self.title = t
    def set_code(self, c): self.code = c
    '''
